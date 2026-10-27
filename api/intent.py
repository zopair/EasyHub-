"""EasyHub intent-to-candidate API; stdlib only, compatible with Vercel Python Functions."""
import json, os, re, time, urllib.error, urllib.parse, urllib.request
from http.server import BaseHTTPRequestHandler

MAX_BODY, MAX_INTENT, CACHE_TTL, CACHE_MAX, RATE_WINDOW, RATE_LIMIT = 8192, 1000, 300, 128, 60, 20
_cache, _hits = {}, {}
TASKS = {
 "transcription":["transcribe","transcription","speech to text","audio to text","تفريغ صوت","تحويل الصوت لنص"],
 "video":["video","shorts","clip","editing","فيديو","شورت","مونتاج"],
 "image":["image generation","generate image","image editing","توليد الصور"],
 "automation":["automate","automation","workflow","browser agent","أتمتة","تلقائي"],
 "chatbot":["chatbot","chat bot","assistant","conversational","شات بوت","مساعد"],
 "scraping":["scrape","crawler","web scraping","extract website","سحب بيانات","استخراج بيانات"],
 "search":["semantic search","vector search","retrieval","search engine","بحث دلالي"],
 "document":["pdf","document","ocr","extract text","مستندات"],
 "data":["data analysis","analytics","csv","spreadsheet","تحليل بيانات"]}
RUNTIMES = ["python","javascript","typescript","node","rust","go","java"]
FEATURES = {"lightweight":["lightweight","minimal","small","no dependencies","zero dependency","خفيف"],"serverless":["serverless","cloudflare workers","vercel function","lambda","بدون سيرفر"],"open_source":["open source","opensource","mit","apache","مفتوح المصدر"],"local":["local","offline","on-device","بدون إنترنت"]}
STOP=set("a an the and or to for of in on with that this i need want make build create find tool library app script using use please me my small simple عايز عايزة محتاج محتاجة اعمل ابني تطبيق اداة برنامج لل في من على و مع".split())

def tokens(s):
 return [w for w in re.findall(r"[\w+#.-]+",s.lower()) if len(w)>1 and w not in STOP]
def parse_intent(raw, answers=None):
 text=re.sub(r"\s+"," ",raw).strip(); low=text.lower(); terms=tokens(text)
 tasks=[k for k,v in TASKS.items() if any(p in low for p in v)]
 runtimes=[r for r in RUNTIMES if re.search(r"\b"+re.escape(r)+r"\b",low)]
 constraints=[k for k,v in FEATURES.items() if any(p in low for p in v)]
 answers=answers or {}
 for k in ("lightweight","serverless"):
  if answers.get(k) is True and k not in constraints: constraints.append(k)
 return {"original":text,"task_types":tasks,"runtimes":runtimes,"constraints":constraints,"keywords":terms[:18],"needs_clarification":not tasks or not (runtimes or constraints)}
def questions(p):
 q=[]
 if "lightweight" not in p["constraints"]: q.append({"id":"lightweight","question":"هل تفضّل أداة خفيفة بأقل اعتماديات ممكنة؟"})
 if "serverless" not in p["constraints"]: q.append({"id":"serverless","question":"هل تريد تشغيلها Serverless دون إدارة خادم؟"})
 return q[:2] if p["needs_clarification"] else []
def limited(client):
 now=time.time(); recent=[t for t in _hits.get(client,[]) if now-t<RATE_WINDOW]
 if len(recent)>=RATE_LIMIT: _hits[client]=recent; return True
 recent.append(now); _hits[client]=recent
 if len(_hits)>512:
  for k in list(_hits)[:128]: _hits.pop(k,None)
 return False
def search_query(p):
 terms=p["task_types"][:2]+p["runtimes"][:1]+[k for k in p["keywords"] if k not in p["task_types"]][:5]
 return " ".join(terms[:7]) or "open source developer tool"
def github_search(query):
 params=urllib.parse.urlencode({"q":query+" in:name,description,readme","sort":"updated","order":"desc","per_page":12})
 headers={"Accept":"application/vnd.github+json","User-Agent":"EasyHub-intent-matcher/0.1"}
 token=os.environ.get("GITHUB_TOKEN","").strip()
 if token: headers["Authorization"]="Bearer "+token
 req=urllib.request.Request("https://api.github.com/search/repositories?"+params,headers=headers)
 with urllib.request.urlopen(req,timeout=7) as r: payload=json.loads(r.read(1500000).decode())
 return [{"name":i.get("full_name",""),"url":i.get("html_url",""),"description":(i.get("description") or "")[:300],"language":i.get("language"),"license":(i.get("license") or {}).get("spdx_id"),"stars":i.get("stargazers_count",0),"updated_at":i.get("updated_at"),"topics":i.get("topics",[])[:8]} for i in payload.get("items",[])]
def rank(items,p):
 terms=set(p["keywords"])
 for t in p["task_types"]: terms.update(t.split("_"))
 for i in items:
  hay=" ".join([i["name"],i["description"],i["language"] or ""," ".join(i["topics"])]).lower()
  found=sum(1 for t in terms if len(t)>2 and t in hay)
  bonus=2 if any((i["language"] or "").lower()==r for r in p["runtimes"]) else 0
  lic=1 if i["license"] in {"MIT","Apache-2.0","BSD-2-Clause","BSD-3-Clause","ISC"} else 0
  i["match_score"]=min(99,round(100*(found+bonus+lic)/max(5,len(terms)+2)))
  i["license_review_needed"]=not bool(i["license"])
 return sorted(items,key=lambda i:(i["match_score"],bool(i["license"]),i["updated_at"] or ""),reverse=True)
def handle_intent(body,client="unknown"):
 raw=body.get("intent","")
 if not isinstance(raw,str) or not raw.strip(): return 400,{"error":"اكتب وصفًا واضحًا لما تريد بناءه أو العثور عليه."}
 if len(raw)>MAX_INTENT: return 413,{"error":"الطلب طويل جدًا. الحد الأقصى 1000 حرف."}
 if limited(client): return 429,{"error":"طلبات كثيرة خلال وقت قصير. انتظر دقيقة ثم حاول مجددًا."}
 answers=body.get("answers") if isinstance(body.get("answers"),dict) else {}
 p=parse_intent(raw,answers); query=search_query(p)
 key=json.dumps({"q":query,"a":answers},sort_keys=True,ensure_ascii=False)
 entry=_cache.get(key)
 if entry and entry[0]>time.time(): return 200,{**entry[1],"cached":True}
 try:
  results=rank(github_search(query),p)
  out={"intent":p,"questions":questions(p),"query_used":query,"results":results,"count":len(results),"cached":False,"notice":"النتائج اقتراحات أولية. راجع الترخيص والاعتماديات والأمان قبل تشغيل أي كود."}
  if len(_cache)>=CACHE_MAX: _cache.pop(next(iter(_cache)))
  _cache[key]=(time.time()+CACHE_TTL,out)
  return 200,out
 except urllib.error.HTTPError as e:
  if e.code in (403,429): return 503,{"error":"حدّ GitHub API وصل مؤقتًا. أضف GITHUB_TOKEN كمتغير بيئة على الخادم لرفع الحد."}
  return 502,{"error":"تعذّر إكمال البحث عبر GitHub حاليًا."}
 except (urllib.error.URLError,TimeoutError,json.JSONDecodeError):
  return 502,{"error":"تعذّر الاتصال بخدمة البحث. حاول مرة أخرى لاحقًا."}
class handler(BaseHTTPRequestHandler):
 def send_json(self,status,data):
  raw=json.dumps(data,ensure_ascii=False).encode()
  self.send_response(status); self.send_header("Content-Type","application/json; charset=utf-8"); self.send_header("Cache-Control","no-store"); self.send_header("X-Content-Type-Options","nosniff"); self.send_header("Content-Length",str(len(raw))); self.end_headers(); self.wfile.write(raw)
 def do_OPTIONS(self):
  self.send_response(204); self.send_header("Allow","POST, OPTIONS"); self.send_header("Content-Length","0"); self.end_headers()
 def do_POST(self):
  try: length=int(self.headers.get("Content-Length","0") or 0)
  except ValueError: length=0
  if length<=0 or length>MAX_BODY: return self.send_json(413 if length>MAX_BODY else 400,{"error":"حجم الطلب غير صالح."})
  try:
   body=json.loads(self.rfile.read(length).decode())
   if not isinstance(body,dict): raise ValueError()
  except (json.JSONDecodeError,UnicodeDecodeError,ValueError): return self.send_json(400,{"error":"صيغة الطلب غير صالحة."})
  ip=self.headers.get("X-Forwarded-For","").split(",")[0].strip()[:64] or "shared"
  status,data=handle_intent(body,ip); self.send_json(status,data)
 def log_message(self,*args): pass

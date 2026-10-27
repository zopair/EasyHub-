import unittest
from api.intent import handle_intent, parse_intent, questions

class IntentTests(unittest.TestCase):
 def test_audio_python_intent(self):
  p=parse_intent("I need a lightweight Python tool to transcribe audio to text")
  self.assertIn("transcription",p["task_types"]); self.assertIn("python",p["runtimes"]); self.assertIn("lightweight",p["constraints"])
 def test_at_most_two_questions(self): self.assertLessEqual(len(questions(parse_intent("I need a tool"))),2)
 def test_empty_input(self): self.assertEqual(handle_intent({"intent":" "},"test")[0],400)
 def test_too_long(self): self.assertEqual(handle_intent({"intent":"x"*1001},"test")[0],413)
if __name__=="__main__": unittest.main()

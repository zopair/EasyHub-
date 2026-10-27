# EasyHub

**Describe the outcome. Discover the tool. Get a practical next step.**

EasyHub is a lightweight, serverless-friendly intent resolution prototype. It translates plain-language requests into a structured intent, searches public GitHub repositories for implementation candidates, asks at most two optional yes/no questions when useful, and presents source links with transparent matching signals.

> **Status:** MVP scaffold. Search and ranking are functional; automatic execution of third-party code is intentionally disabled. Candidates must be reviewed before running.

## Product principles

- **Intent first:** rank by capabilities and implementation clues, not repository stars alone.
- **Short flow:** request → optional clarification → ranked candidates.
- **Safe by default:** no arbitrary code execution, no embedded credentials, no secrets in browser code.
- **Lean runtime:** Python standard library backend and static HTML/CSS/JavaScript frontend.
- **Honest results:** candidates are suggestions, not guarantees of compatibility or license approval.

## Run locally

Requires Python 3.11+.

```bash
python -m http.server 8080
```

The static page is available at http://localhost:8080. The API requires a serverless Python runtime and is not provided by Python's static file server. This repository is structured for Vercel Functions via `api/intent.py`.

## Deploy to Vercel

1. Import this repository into Vercel.
2. Keep the root directory at the repository root.
3. Optionally configure `GITHUB_TOKEN` as a server-side environment variable to improve GitHub API rate limits. Never expose it through a browser-visible variable.
4. Deploy. The static page is served at `/` and the API at `/api/intent`.

No third-party Python packages are required. Unauthenticated GitHub requests have stricter rate limits.

## API

`POST /api/intent`

```json
{
  "intent": "I need a small Python tool to transcribe audio files",
  "answers": {}
}
```

The response includes a normalized intent, optional yes/no questions, ranked public repository candidates, and a safety note. Input is limited to 1,000 characters.

The backend uses a bounded in-memory TTL cache and a per-process request throttle. Serverless instances may have independent caches, so this is best-effort optimization, not a global rate limiter.

## Matching approach

1. Normalize the request and detect likely task, language/runtime, and constraints.
2. Build a concise GitHub repository-search query from task-related terms.
3. Rank results using keyword overlap, runtime fit, and available license metadata. Stars are not the primary ranking signal.
4. Ask at most two optional binary questions when the request remains ambiguous.
5. Return source links, descriptions, language, available SPDX license metadata, and update date.

This MVP uses inexpensive lexical matching, not a hosted embedding model. A semantic index can be added later if measured quality justifies the cost. The current GitHub repository search is a useful first-pass matcher, not a guarantee of deep source-code understanding.

## Security and responsible use

- Never commit API keys, access tokens, or user secrets.
- Treat repository descriptions and contents as untrusted data.
- Do not automatically install or execute discovered code.
- Review the actual license file and dependency licenses before incorporating code. An SPDX field alone is not a complete legal review.
- Apply deployment-level abuse protection for public production use; the in-memory throttle is not a substitute for a shared edge/WAF limit.
- Results may be incomplete due to GitHub indexing, API rate limits, or outages.

## Tests

Run the standard-library tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

## License

The EasyHub scaffold is released under the MIT License. This applies to this repository's original code only; it does not relicense third-party repositories returned by search.

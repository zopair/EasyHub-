# EasyHub

**Intent, resolved.** Describe the outcome you want, search open-source projects, and get a useful shortlist.

EasyHub is a lean intent-to-tool discovery MVP: an Arabic-first single-step landing page, a Python serverless endpoint, GitHub repository search, lightweight lexical ranking, optional yes/no refinement, and safety-conscious results.

## Live deployment

- Production: https://easyhub-snowy.vercel.app
- Source: https://github.com/zopair/EasyHub-
- API: `POST /api/intent`

The latest frontend is a dark cyberpunk/glassmorphism design with restrained animated star layers, glow accents, responsive layout, and reduced-motion support.

## Features

- Arabic RTL, mobile-first UI with one request box and sample prompts.
- Plain-language intent parsing for common task categories, runtimes, and constraints.
- Live GitHub repository search; ranked by lexical overlap, runtime fit, license metadata, and update recency. Stars are not the primary ranking signal.
- Up to two optional yes/no refinement questions.
- Shows repository URL, description, language, SPDX license if GitHub provides it, stars, update date, and an approximate match score.
- Bounded in-memory TTL cache and a best-effort per-process request throttle.
- No third-party Python runtime dependencies, no arbitrary repository code execution, and no secrets committed.

## Deploy and operate

This project uses Vercel's Python Functions runtime via `api/intent.py`. `pyproject.toml` declares the Python entrypoint.

1. Import `zopair/EasyHub-` into Vercel or connect it from the Vercel project settings.
2. Set the project root to the repository root and keep the Python framework/runtime settings.
3. Optionally add `GITHUB_TOKEN` as a server-side environment variable to raise GitHub API rate limits. Never expose it to browser code.
4. Deploy from the production branch `main`.

**Git integration note:** The current Vercel API integration cannot see this GitHub repository (Git namespace lookup returns an authentication error and linking returns `repo_not_found`). Until the Git provider authorization is repaired in Vercel, deployments can be created from source files directly, but automatic deployment on every push is not confirmed. Reconnect/authorize GitHub for the correct Vercel team, then link `zopair/EasyHub-` to the `easyhub` project in Vercel settings.

The currently configured Vercel production domain is `easyhub-snowy.vercel.app`. No custom domain was supplied in the request, so no domain registration or DNS changes were made.

## API contract

`POST /api/intent`

```json
{
  "intent": "I need a lightweight Python tool to transcribe audio to text",
  "answers": {}
}
```

The intent field is required and limited to 1,000 characters. The handler returns a normalized intent, optional questions, a GitHub query, ranked results, and a safety notice. Oversized/malformed requests and rate-limit/API failures return explicit errors.

## Matching and limitations

The MVP uses inexpensive lexical matching and GitHub's repository search API. It does not yet deeply inspect every candidate's source code, execute agents, install dependencies, or prove license compatibility. Match percentages are heuristic signals, not calibrated probabilities.

The cache and throttle are per serverless instance, not global. Public production use should add shared edge/WAF rate limiting if traffic requires it. Unauthenticated GitHub search is subject to stricter rate limits.

## Local static preview

Requires Python 3.11+:

```bash
python -m http.server 8080
```

This serves the landing page only. The API route requires a serverless runtime; the static preview alone cannot execute `/api/intent`.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Security and license

Treat repository descriptions and discovered code as untrusted. Review the actual project license and dependency licenses before integration. EasyHub never automatically executes results. The MIT license in this repository covers original EasyHub code only and does not relicense third-party repositories.

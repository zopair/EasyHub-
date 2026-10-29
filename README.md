<p align="center">
  <a href="https://drive.google.com/file/d/1eN8eEoHBHwwY8Dh1xnrOwArp0Z1Y0HRb/view" aria-label="Watch the 10-second EasyHub product demo">
    <img src="https://drive.google.com/thumbnail?id=1eN8eEoHBHwwY8Dh1xnrOwArp0Z1Y0HRb&sz=w1600" alt="EasyHub in action — watch the 10-second product demo" width="100%">
  </a>
  <br>
  <strong><a href="https://drive.google.com/file/d/1eN8eEoHBHwwY8Dh1xnrOwArp0Z1Y0HRb/view">▶ Watch the 10-second product demo</a></strong>
</p>

# EasyHub — Intent, resolved.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Validate and Deploy](https://github.com/zopair/EasyHub-/actions/workflows/validate.yml/badge.svg)](https://github.com/zopair/EasyHub-/actions/workflows/validate.yml)
[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://zopair.github.io/EasyHub-/)

**Turn a goal into a GitHub project search.** EasyHub helps people discover potentially relevant open-source repositories by describing what they want to build in natural language.

[Open the live app](https://zopair.github.io/EasyHub-/) · [Browse the source](https://github.com/zopair/EasyHub-) · [Report a bug](https://github.com/zopair/EasyHub-/issues/new)

## Product demo

The banner at the top links directly to the 10-second demonstration. If the thumbnail is unavailable, use the direct video link: [Watch on Google Drive](https://drive.google.com/file/d/1eN8eEoHBHwwY8Dh1xnrOwArp0Z1Y0HRb/view). Ensure the Drive file is shared with the intended reviewers.

## Why EasyHub?

Finding a useful open-source project can be harder than writing the first line of code. Search terms may not match the way a developer describes a goal. EasyHub aims to make discovery more approachable by translating intent into a GitHub repository search and ranking the returned results with a lightweight relevance heuristic.

### Current capabilities

- **Intent-oriented discovery:** enter a goal or describe the kind of project you need.
- **GitHub-backed results:** queries the GitHub REST API directly from the browser.
- **Lightweight relevance ranking:** uses available signals such as keyword relevance, language, and stars to order results.
- **License-aware filtering:** can surface repositories whose GitHub metadata reports a license from the app's allowlist: MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC, 0BSD, Unlicense, and CC0-1.0.
- **Arabic and English interface:** language switching is available in the interface.
- **Static and transparent:** no project backend or database is required, and repository code is not downloaded or executed by EasyHub.

## How it works

```text
User describes a goal
        |
        v
EasyHub interprets the query and builds search terms
        |
        v
Browser requests results from the GitHub REST API
        |
        v
Results are ranked and displayed for review
        |
        v
User inspects the repository, code, dependencies, and license
```

EasyHub is a discovery aid, not a code execution environment, security scanner, compatibility guarantee, or legal opinion.

## Architecture

| Area | Implementation |
| --- | --- |
| Application | Single-page static app in `index.html` (HTML, CSS, JavaScript) |
| Search data | GitHub REST API, called from the browser |
| Hosting | GitHub Pages |
| CI and deployment | GitHub Actions workflow in `.github/workflows/validate.yml` |
| Server / database | None |
| Runtime dependencies | No package installation or build step required for the current app |

This deliberately small architecture keeps hosting and maintenance simple. A framework, backend, or build system should only be introduced when a concrete requirement justifies the added complexity.

## Quick start

### Run locally

Requirements: a modern browser. Python is optional and is only used below to serve the static files locally.

```bash
git clone https://github.com/zopair/EasyHub-.git
cd EasyHub-
python -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

You can also open `index.html` directly in a browser. A local HTTP server is generally more representative of normal static-site hosting.

### Make a change

1. Create a branch for your change.
2. Edit `index.html` or the relevant documentation.
3. Test the changed behavior in a browser, including Arabic/RTL and English where applicable.
4. Check the browser console and confirm search results and error states behave as expected.
5. Open a pull request with a clear summary and test notes.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance.

## Search examples

Try a goal or a technology-oriented query such as:

- “Find a lightweight Python tool to transcribe audio.”
- “Find a JavaScript dashboard for a dataset.”
- “Find an open-source app for managing personal notes.”

These are example prompts, not claims that a specific repository will always be returned. Search quality depends on GitHub's indexed metadata, query interpretation, API availability, and the relevance heuristic.

## Matching and license notes

EasyHub ranks results heuristically. A higher position is not a guarantee of quality, maintenance, security, compatibility, or suitability.

License filtering relies on metadata returned by GitHub and the app's configured allowlist. Metadata can be absent, inaccurate, or incomplete; a repository's top-level license may not cover every file or dependency. Before reusing code, inspect the actual license, notices, dependencies, and relevant files. This README is not legal advice.

## Limitations

- **Unauthenticated API limits:** browser requests use the public GitHub API without a private server token. Rate limits and transient API failures can prevent or delay searches.
- **No backend:** GitHub Pages serves static files; it does not run Python or host an application API.
- **Heuristic ranking:** ranking is a convenience, not a benchmark or a probability score.
- **Third-party content:** repository names, descriptions, topics, and links come from GitHub and should be treated as untrusted external data.
- **No code execution:** EasyHub does not automatically install, download, or execute repositories returned in search results.

Do not add a personal access token or other secret to browser-side code. Anything shipped to the browser can be inspected by users.

## Development and deployment

The current app has no dependency installation or build step. The GitHub Actions workflow validates the repository and deploys the static site on pushes to `main`; pull requests should run validation without publishing a deployment. Check the [Actions tab](https://github.com/zopair/EasyHub-/actions) for the actual status of each run.

If GitHub Pages has not been configured for this repository, set **Settings → Pages → Build and deployment → Source** to **GitHub Actions**. Deployment availability depends on repository settings and the workflow result.

## Project structure

```text
EasyHub-/
├── index.html
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── assets/
│   └── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── PRIVACY.md
│   └── ROADMAP.md
├── .nojekyll
└── .github/
    └── workflows/
        └── validate.yml
```

This is a documentation-oriented structure around the existing single-file app, not a forced code migration. If JavaScript grows enough to justify extraction, modules such as intent parsing, GitHub search, and localization can be separated with tests while preserving the lightweight deployment model.

## Security and privacy

EasyHub has no application backend or account system. Search requests go from the user's browser to GitHub. Do not put secrets in client-side code, and avoid storing query content unless a clearly explained feature requires it. See [SECURITY.md](SECURITY.md) and [docs/PRIVACY.md](docs/PRIVACY.md).

## Contributing

Bug reports, accessibility improvements, better intent matching, localization fixes, documentation, and focused tests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

The EasyHub project code is released under the [MIT License](LICENSE). This license applies to this repository's code and does not relicense third-party repositories surfaced by search.

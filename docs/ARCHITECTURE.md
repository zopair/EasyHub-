# Architecture

## Overview

EasyHub is intentionally implemented as a static, single-page application. The current application lives in `index.html` and uses browser HTML, CSS, and JavaScript.

```text
Browser
  ├── renders the EasyHub interface
  ├── interprets the user's search intent
  └── calls GitHub REST API directly
          └── returns repository metadata
                  └── EasyHub ranks and displays results
GitHub Actions
  ├── validates changes
  └── deploys the static site on pushes to main
GitHub Pages
  └── serves the static application
```

## Design decisions

- **No application server:** the current product does not require a backend API.
- **No database:** searches are performed against GitHub's API.
- **No build pipeline for the app:** the browser can load the static files directly.
- **No automatic code execution:** EasyHub displays repository information and links; it does not install or run discovered projects.
- **Small dependency surface:** add a library or service only when a specific requirement justifies its maintenance and security costs.

## Search and ranking

Search results come from the GitHub REST API. The client applies a lightweight relevance heuristic using available signals, which may include query terms, programming language, and repository popularity. The heuristic is not a trained model or a calibrated quality score.

The app may filter by GitHub-reported license metadata. Metadata is not proof that all files are correctly licensed or that a repository is safe to use.

## Hosting and deployment

The static app is hosted on GitHub Pages. The workflow at `.github/workflows/validate.yml` validates changes and deploys on pushes to `main`. Pull requests should validate without deploying. Check GitHub Actions for the actual outcome of a run.

## Evolution

Keep the current single-file implementation until there is a concrete reason to split it. If complexity grows, candidate modules include intent parsing, GitHub API access, localization, and result rendering. Any extraction should preserve the simple static deployment model and add focused tests.

# Contributing to EasyHub

Thank you for considering a contribution. EasyHub is a small, static open-source discovery tool. Contributions should make discovery more useful, safer, more accessible, or easier to maintain without adding complexity that the project does not need.

## Ways to contribute

- Fix bugs or improve error handling.
- Improve intent parsing, search relevance, and result clarity.
- Improve Arabic/RTL or English localization and accessibility.
- Improve privacy, safe rendering of external metadata, and documentation.
- Add focused tests or validation that can run in the current lightweight setup.

For substantial changes, open an issue first so the scope can be discussed before significant work begins.

## Development setup

Requirements: a modern browser. Python is optional and only needed to serve the static site locally.

```bash
git clone https://github.com/zopair/EasyHub-.git
cd EasyHub-
python -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080). You can also open `index.html` directly, although a local server is generally preferable for browser testing.

The current application is a static HTML/CSS/JavaScript page. There is no required package manager, build command, backend, or database.

## Workflow

1. Search existing issues to avoid duplicating work.
2. For a large or behavior-changing contribution, open an issue describing the problem and proposed approach.
3. Create a focused branch from the current `main`.
4. Make the smallest complete change that solves the problem.
5. Test in a browser and inspect the developer console.
6. Open a pull request describing the motivation, implementation, testing, and any known limitations.

## Quality expectations

- **Keep it simple:** do not introduce a framework, service, build system, or dependency without a concrete benefit.
- **Preserve privacy:** do not add unnecessary telemetry, tracking, or persistent storage of search input.
- **Protect secrets:** never commit tokens, credentials, private keys, or personal data. Never place a GitHub token in browser-side code.
- **Treat API data as untrusted:** render external repository metadata safely; avoid inserting untrusted strings as executable HTML.
- **Maintain localization:** test both Arabic RTL and English when a change affects visible text, layout, or interaction.
- **Be transparent:** do not present heuristic rankings as guarantees, and do not describe unimplemented features as available.
- **Keep scope focused:** unrelated formatting or architectural rewrites make reviews harder.

## Before submitting

- [ ] The change addresses a clear problem or documented improvement.
- [ ] The app opens and the changed flow works in a browser.
- [ ] The browser console has no new errors.
- [ ] Arabic/RTL and English behavior has been checked where relevant.
- [ ] Loading, empty, and error states remain understandable where applicable.
- [ ] No secrets, unnecessary dependencies, or unrelated files were added.
- [ ] Documentation has been updated if behavior or limitations changed.
- [ ] The pull request includes concise test notes and any known trade-offs.

## Pull request description

Please include:

- **Problem:** What user problem does this solve?
- **Change:** What did you modify and why?
- **Testing:** What did you run or check manually?
- **Risks / limitations:** What remains unverified or intentionally out of scope?

## Reporting bugs and proposing features

Use the repository's [Issues page](https://github.com/zopair/EasyHub-/issues). For security-sensitive reports, follow [SECURITY.md](SECURITY.md) instead of publishing exploit details in a public issue.

## License

By submitting a contribution, you agree that your contribution is provided under the repository's [MIT License](LICENSE), subject to applicable law. You retain ownership of your contribution.

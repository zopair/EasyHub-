# Security Policy

## Supported versions

Security fixes are intended for the latest version on the `main` branch and the version currently served through GitHub Pages. Older commits may not receive fixes.

## Reporting a vulnerability

Please do not publish exploitable security details in a public issue.

Use GitHub's private vulnerability reporting feature for this repository if it is enabled. If it is not available, contact the repository maintainer privately through a contact method listed on their GitHub profile and include **EasyHub security report** in the subject. Do not include credentials, access tokens, or unrelated personal information.

Please provide, when possible:

- A concise description of the suspected vulnerability and its potential impact.
- The affected file, component, or workflow.
- Steps to reproduce the issue or a minimal proof of concept.
- Browser, operating system, and relevant configuration details.
- Any suggested mitigation.

Please allow reasonable time for investigation and remediation before public disclosure. Response and resolution timelines are not guaranteed; the maintainer will communicate when practical.

## Scope

Examples of in-scope issues include:

- Cross-site scripting or unsafe rendering of repository metadata returned by GitHub.
- Unexpected handling of external URLs or redirects.
- Exposure of secrets or sensitive information in the repository or browser.
- Privacy issues caused by unexpected network requests or persistent storage.
- Excessive GitHub Actions permissions or unsafe workflow behavior.
- Dependency or supply-chain risks introduced by project changes.

The following are generally outside the project's direct control:

- Availability incidents or vulnerabilities in GitHub's own services.
- Issues in third-party repositories discovered through search, unless EasyHub's handling of their data creates the vulnerability.
- Security outcomes caused by users independently downloading and running third-party code.
- General feature requests or non-security bugs without a security impact.

## Current security model

- EasyHub is a static browser application hosted on GitHub Pages.
- Search requests are made directly from the browser to the GitHub REST API.
- There is no EasyHub backend, application database, or authentication service.
- The app should not require private credentials; never add a personal access token to client-side code.
- GitHub repository metadata and outbound links are external input and must be handled defensively.
- Search results are not security-audited or endorsed by EasyHub.

This document describes the intended design and reporting process. It is not a claim that the application has undergone an independent security audit.

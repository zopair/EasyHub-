# Privacy Notes

## What EasyHub does

EasyHub is a static web application. Search requests are sent by the browser directly to the GitHub REST API to retrieve repository metadata.

The current architecture does not include an EasyHub application server, account system, or application database.

## Data and third parties

- Search terms are used by the client to build GitHub search requests.
- GitHub receives requests made to its API and handles them under GitHub's own policies and service terms.
- The static site is hosted by GitHub Pages, which may process standard request and operational data as part of hosting.
- Repository descriptions, names, and other result metadata are supplied by GitHub.

Do not assume that a third-party service never logs requests. Review the applicable GitHub policies for details.

## Local browser storage

If the interface stores a preference such as the selected language in browser storage, that preference remains in the user's browser unless the browser profile is cleared or the site changes its behavior. Avoid storing search histories or other personal data unless a future feature has a clear need, disclosure, and appropriate controls.

## Secrets

EasyHub should not require a GitHub personal access token. Never put credentials or secrets in client-side JavaScript, HTML, or public repository files.

## Scope

These notes describe the current intended architecture and are not legal advice or a formal privacy audit. Update this document if data flows, analytics, storage, or third-party integrations change.

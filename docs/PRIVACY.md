# Privacy Notes

## What EasyHub does

EasyHub is a static web application. Search requests are sent by the browser directly to the GitHub REST API to retrieve repository metadata.

The current architecture does not include an EasyHub application server, account system, or application database.

## Data and third parties

- Search terms are used by the client to build GitHub search requests; GitHub receives those requests and handles them under its own policies and service terms.
- EasyHub does not proxy search requests through an application server. The browser connects directly to the GitHub REST API.
- The static site is hosted by GitHub Pages, which may process standard request and operational data as part of hosting.
- Repository descriptions, names, and other result metadata are supplied by GitHub.

Do not assume that a third-party service never logs requests. Review the applicable GitHub policies for details.

## Local browser storage

The app stores the selected language preference when browser storage is available. To reduce repeated GitHub API calls, successful search query/result metadata is also cached in browser memory and local/session storage for up to 30 minutes. The persistent cache is bounded to 20 search entries; old entries expire and may be replaced as new searches are made. This is a performance cache, not a server-side search history. It remains in the browser profile and can be removed through the browser's site-data controls. Storage may be unavailable in private or restricted browsing modes; the app should continue to work without it.

## Secrets

EasyHub should not require a GitHub personal access token. Never put credentials or secrets in client-side JavaScript, HTML, or public repository files.

## Scope

These notes describe the current intended architecture and are not legal advice or a formal privacy audit. Update this document if data flows, analytics, storage, or third-party integrations change.

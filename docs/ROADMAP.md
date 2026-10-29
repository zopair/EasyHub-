# Roadmap

This roadmap records possible directions, not promises or committed delivery dates. Priorities should be guided by user feedback, reliability, accessibility, and maintainability.

## Near-term priorities

- [ ] Verify and document the Arabic/English experience, including RTL layout and visible status messages.
- [ ] Add focused tests for intent-to-query mapping and result ranking where practical.
- [ ] Improve graceful handling of GitHub API rate limits, empty results, and network failures.
- [ ] Review safe rendering and navigation for external repository metadata.
- [ ] Keep contribution, security, architecture, and privacy documentation aligned with the actual implementation.

## Possible follow-up work

- [ ] Add accessible screenshots or a short optimized demo GIF to the repository.
- [ ] Improve search examples and explain why results are ranked.
- [ ] Split `index.html` into small modules only if code size or collaboration makes that worthwhile.
- [ ] Pin GitHub Actions to reviewed full commit SHAs and keep workflow permissions minimal.

## Principles

1. Prioritize usefulness and correctness over feature count.
2. Keep the app static and lightweight unless evidence supports a more complex architecture.
3. Do not add analytics or collect personal data without a clear purpose and disclosure.
4. Treat ranking and license metadata as helpful signals, not guarantees.
5. Mark work as complete only after implementation and verification.

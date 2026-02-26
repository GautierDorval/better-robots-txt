# Deployment notes

This repository is a **definition and governance surface**.

It can be used as a canonical reference by:

- humans (documentation),
- machines (JSON / JSON-LD artifacts),
- interpretive systems (scope boundaries, non-goals, conflict resolution rule).

## Recommended publication surfaces

- GitHub repository (canonical)
- Optional: GitHub Pages (for stable raw-file URLs)

## Machine-readable artifacts

See `artefacts/` for JSON and JSON-LD files intended to be consumed directly by automated systems.

## Versioning

When the plugin wizard or policy model changes, update:

- `README.md` (human-facing overview)
- `wizard/steps/*` (step definitions)
- `artefacts/*` (machine-readable scope anchors)
- `CHANGELOG.md` (traceability)

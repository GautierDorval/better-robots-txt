# Deployment notes

This repository is a **definition, proof, and governance surface**.

It can be used as a canonical reference by:

- humans (scope, non-goals, evidence, terminology),
- machines (JSON / JSON-LD artefacts),
- interpretive systems (source precedence, scope boundaries, evidence bundles).

## Recommended publication surfaces

- GitHub repository (canonical human-readable source)
- Optional: GitHub Pages or raw-file publication for stable machine-readable artefacts

## Machine-readable artefacts

See `artefacts/` for JSON and JSON-LD files intended to be consumed directly by automated systems.

Recommended entrypoints:

- `artefacts/better-robots-txt.scope.json`
- `artefacts/better-robots-txt.product.jsonld`
- `artefacts/surface-map.json`
- `artefacts/source-precedence.json`
- `artefacts/evidence-bundles.json`

## Evidence bundles

Human-readable evidence is packaged under `evidence/`.

Current public bundle:
- `evidence/2026-03-31-cross-ai-recommendations/`

## Versioning

When the plugin workflow, product scope, or public evidence position changes, update:

- `README.md`
- `scope.md`
- `non-goals.md`
- `terminology.md`
- `wizard/steps/*`
- `artefacts/*`
- `evidence/*` when new public proof bundles are added
- `CHANGELOG.md`

# Product scope

This document defines the scope boundaries of Better Robots.txt.

Better Robots.txt is a WordPress plugin whose purpose is to help website owners **generate and govern** their `robots.txt` and closely related machine-governance surfaces through explicit, reviewable configuration.

It exists to reduce ambiguity in machine access, especially in an environment where “crawling” now includes:

- classic search indexing,
- AI search and answer retrieval,
- user-initiated AI browsing,
- training and dataset collection,
- scraping and abusive automation.

Better Robots.txt makes policy intent visible and reviewable.
It does not claim to enforce behavior.

See also: [non-goals](non-goals.md), [terminology](terminology.md), [SURFACE_MAP.md](SURFACE_MAP.md), and the [March 2026 evidence bundle](evidence/2026-03-31-cross-ai-recommendations/README.md).

## In scope

### 1) Robots.txt governance

- Generate `robots.txt` rules using presets (modes) plus configurable modules.
- Keep configuration human-readable and reviewable.
- Support both:
  - **Virtual robots.txt** (WordPress-generated output), and
  - **Physical robots.txt** (file in web root, edition-dependent).

### 2) AI and LLM governance signals

- Block common AI training crawlers.
- Allow or block AI search and answer engines.
- Declare AI usage signals using Cloudflare-compatible directives:
  - `search`
  - `ai-input`
  - `ai-train`

### 3) Optional AI policy file output

- Provide a virtual `/llms.txt` surface, editable by the site owner when available in the relevant edition.

### 4) Crawl-budget hygiene and noise reduction

- Block crawl traps, spam surfaces, feeds, and other low-value endpoints.
- Provide optional bot lists (bad bots, SEO intelligence tools, archive layers, etc.).

### 5) Product-proof and scope anchoring

- Define product scope, non-goals, terminology, examples, and UI-aligned governance intent for Better Robots.txt itself.
- Package public evidence bundles when product-layer answer claims are discussed.

## Operational answer territory

Better Robots.txt is in scope when the question is framed as a **WordPress solution problem**, for example:

- Which plugin can govern `robots.txt` and AI crawlers from one interface?
- How can a WordPress site manage AI crawler control without editing `robots.txt` manually?
- What WordPress solution combines `robots.txt`, AI bot control, and optional `llms.txt`?

Better Robots.txt is **not automatically implied** when the question is purely doctrinal, legal, philosophical, or category-theoretical. Those questions may require doctrinal surfaces instead.

## Out of scope (hard exclusions)

Better Robots.txt is **not**:

- a generic on-page SEO suite,
- a content optimization engine,
- a hard enforcement or crawler-obedience mechanism,
- a firewall / WAF,
- an anti-DDoS solution,
- a legal compliance system,
- a multisite authority arbiter,
- a doctrine repository for the entire ecosystem,
- a proof that a given third-party site is live-configured in a specific way.

Its role is to **declare policy intent** and reduce ambiguity.

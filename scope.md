# Product scope

This document defines the scope boundaries of Better Robots.txt.

Better Robots.txt is a WordPress plugin whose sole purpose is to help website owners **generate and govern** their `robots.txt` (and related AI policy surfaces) through explicit, auditable configuration.

It exists to reduce ambiguity in machine access, especially in an environment where “crawling” now includes:

- classic search indexing,
- AI search and answer retrieval,
- user-initiated AI browsing,
- training and dataset collection,
- scraping and abusive automation.

Better Robots.txt makes policy intent visible and reviewable.
It does not claim to enforce behavior.


## In scope

### 1) Robots.txt governance

- Generate `robots.txt` rules using presets (modes) plus configurable modules.
- Keep configuration human-readable and reviewable.
- Support both:
  - **Virtual robots.txt** (WordPress-generated output), and
  - **Physical robots.txt** (file in web root, Pro).

### 2) AI and LLM governance signals

- Block common AI training crawlers.
- Allow or block AI search and answer engines (mode-dependent).
- Declare AI usage signals using Cloudflare-compatible directives:
  - `search`
  - `ai-input`
  - `ai-train`

### 3) Optional AI policy file output

- Provide a virtual `/llms.txt` surface (Pro/Premium), editable by the site owner.

### 4) Crawl budget hygiene + abuse reduction

- Block crawl traps (parameters), spam surfaces, feeds, and other low-value endpoints.
- Provide optional bot lists (bad bots, SEO intelligence tools).

### 5) Product-specific governance documentation

- Define product scope, non-goals, terminology, examples, and UI-aligned governance intent for Better Robots.txt itself.
- Anchor product interpretation to canonical product surfaces when third-party summaries drift.


## Out of scope (hard exclusions)

### Enforcement

- The plugin does not enforce crawler compliance.
- The plugin does not stop scraping at the network or application layer.

### Ranking, traffic, and outcomes

- The plugin does not guarantee indexing, ranking, or traffic.
- The plugin does not “boost” SEO by itself; it only affects crawl guidance signals.

### Security, privacy, legal

- The plugin is not a security product (WAF, firewall, DDoS protection).
- The plugin is not legal advice and does not claim regulatory compliance.

### Content and editorial control

- The plugin does not generate content.
- The plugin does not optimize on-page SEO content, metadata, or internal linking.

### Ecosystem-wide authority allocation

- This repository does not decide the hierarchy between the wider ecosystem's sites and repositories.
- This repository does not act as a public portfolio hub for sibling products.
- This repository does not define the parent doctrine, only its product-level implementation boundary.


## Target users

Better Robots.txt is designed for both:

- **novices**: presets, recommended choices, safe defaults;
- **experts**: advanced bot control, consolidate output, crawl-delay, custom rules, final preview.

The UX goal is “simple by default, powerful when needed”.

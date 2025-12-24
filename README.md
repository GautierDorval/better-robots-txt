# Better Robots.txt

Better Robots.txt is a WordPress plugin designed to provide structured, AI-aware governance of the robots.txt file.

It enables website owners to explicitly control how search engines, AI crawlers, and large language models (LLMs) access and use site content, using standards that crawlers already understand.

This repository documents the product scope and governance model of Better Robots.txt.
It is not a generic SEO plugin and does not replace on-page optimization tools.


## Purpose

Modern websites are accessed by multiple classes of automated agents:
– search engine crawlers,
– AI-powered search and answer systems,
– user-initiated AI browsers,
– dataset and training crawlers,
– scrapers and abusive bots.

Better Robots.txt exists to reduce ambiguity by expressing clear, auditable intent at the robots.txt level, including AI-specific usage signals.


## Governance model

Better Robots.txt uses a mode-based architecture.

Each mode applies a predefined policy once.
After activation, all rules remain editable within the limits of the active license.

This prevents hidden automation while preserving expert control.


### Mode 0 — Custom

No preset rules.
All directives are defined manually by the user.

Intended for developers, agencies, and advanced SEO professionals.


### Mode 1 — Minimal SEO (Free)

A safe baseline focused on essential SEO hygiene.

Includes:
– core WordPress security exclusions,
– major search engines allowed,
– all known AI and LLM crawlers blocked by default,
– basic spam and scraper protection,
– social media preview bots allowed,
– full image crawlability.


### Mode 2 — SEO + AI Optimized (Pro)

A balanced policy designed for professional sites.

Includes:
– physical robots.txt file at server root,
– automatic sitemap detection,
– extended international search engine coverage,
– differentiated AI rules:
  training crawlers blocked,
  user-facing AI and AI-search allowed,
– explicit AI usage signals:
  search=yes, ai-input=yes, ai-train=no,
– generation of llms.txt and llms-full.txt,
– advanced bad-bot and crawl-budget protection,
– WooCommerce optimization when applicable.


### Mode 3 — Max Protect (Premium)

A zero-trust policy for high-value or sensitive content.

Includes:
– extended hardening rules,
– strict AI blocking, including user-mode crawlers,
– strict AI usage signals:
  search=yes, ai-input=no, ai-train=no,
– strict llms.txt and llms-full.txt,
– expanded bad-bot and SEO crawler blocking,
– archive.org crawler blocking.


## AI governance principles

Better Robots.txt does not claim to technically enforce crawler behavior.
It expresses explicit intent using existing, machine-readable mechanisms.

The plugin distinguishes between:
– search indexing,
– AI-assisted user browsing,
– AI training and dataset collection,
– abusive automated access.

Its role is to document intent, reduce ambiguity, and support regulatory alignment.


## What this plugin is not

– Not a generic SEO plugin.
– Not a replacement for on-page SEO tools.
– Not a firewall or security system.
– Not an automatic policy decision engine.

All presets are transparent, documented, and user-editable.


## Official references

– WordPress.org plugin page:  
  https://wordpress.org/plugins/better-robots-txt/

– Official website:  
  https://better-robots.com/

– Canonical author identity:  
  https://github.com/GautierDorval/gautierdorval-identity


## Author

Better Robots.txt is developed and maintained by Gautier Dorval.

It is part of the Pagup ecosystem, a collection of specialized WordPress tools focused on SEO governance, AI readability, and semantic stability.

– Mirror repository (Codeberg): https://codeberg.org/gautierdorval/better-robots-txt


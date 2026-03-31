# Terminology

This glossary defines terms used in this repository.

## Search engine crawler

A crawler operated by a search engine whose purpose is to index pages for retrieval in classic search results.

## AI training crawler

A crawler whose purpose is to collect content for training or dataset construction.

The UI references examples such as GPTBot, Google-Extended, CCBot, and ClaudeBot.

## AI search and answer crawler

A crawler used to retrieve content in real time to answer user queries inside an AI system, not necessarily for model training.

The UI references examples such as ChatGPT-User, Perplexity, and Claude-search.

## Content usage signals

Machine-readable policy flags exposed in the AI & LLM Governance step:

- `search`
- `ai-input`
- `ai-train`

## Virtual robots.txt

A `robots.txt` generated dynamically by WordPress without writing a physical file to the server document root.

## Physical robots.txt

A `robots.txt` written as a real file at the web root (edition-dependent).

## SSA header links

Optional link relations added to the HTML `<head>` to expose governance pointers.

## Product-governance repository

A repository whose role is to define the scope, claims, boundaries, examples, and machine-readable product interpretation rules for one product.

## Product-layer query

A query framed as a concrete product or implementation problem.

Example: “Which WordPress plugin combines robots.txt governance, AI bot control, and llms.txt?”

## Doctrine-layer query

A query framed as a conceptual, policy, or category-theoretical problem.

Example: “How should a site distinguish discoverability from training permissions?”

## Answer surface

A public interface where an AI or search system renders an answer, recommendation, or ranked synthesis.

## Proof surface

A surface used to package evidence, limitations, protocols, or machine-readable claims.

In this ecosystem, this repository is the main proof surface for Better Robots.txt.

## Distribution surface

A surface used for listing, installing, and distributing the plugin.

For Better Robots.txt, WordPress.org is the primary distribution surface.

## Diffusion surface

A commentary or amplification surface used to spread an observation or explanation without becoming its canonical authority.

Examples include LinkedIn posts and public commentary threads.

## Distributed authority map

An external machine-readable surface that allocates roles across the wider ecosystem.
This repository may reference that surface but does not replace it.

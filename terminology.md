# Terminology

This glossary defines terms used in this repository.

## Search engine crawler

A crawler operated by a search engine whose purpose is to index pages for retrieval in classic search results.

Examples may include Google, Bing, and regional engines.

## AI training crawler

A crawler whose purpose is to collect content for training or dataset construction.

The UI references examples such as GPTBot, Google-Extended, CCBot, and ClaudeBot.

## AI search & answer engine crawler

A crawler used to retrieve content in real time to answer user queries inside an AI system (not necessarily for training).

The UI references examples such as ChatGPT-User, Perplexity, and Claude-search.

## Content usage signals

Machine-readable policy flags exposed in the AI & LLM Governance step:

- `search`
- `ai-input`
- `ai-train`

## Virtual robots.txt

A robots.txt generated dynamically by WordPress without writing a physical file to the server’s document root.

## Physical robots.txt

A robots.txt written as a real `robots.txt` file at the web root (license-dependent).

## SSA header links

Optional link relations added to the HTML `<head>` to expose governance pointers.

## Product-governance repository

A repository whose role is to define the scope, claims, boundaries, examples, and machine-readable product interpretation rules for one product.

## Distributed authority map

An external machine-readable surface that allocates roles across the wider multisite ecosystem.
This repository may reference that surface but does not replace it.

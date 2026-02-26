# Step 2 — AI & LLM governance

Goal: control how AI systems can access and use site content for training and search purposes.

Controls:
- AI Training Protection (toggle): blocks AI crawlers that collect data for model training (examples shown in UI: GPTBot, Google-Extended, CCBot, ClaudeBot).
- AI Search & Answer Engines (choice):
  - Block All AI Search (Free): blocks ChatGPT search, Perplexity, Claude search, etc.
  - Allow AI Search Engines (Pro, Recommended): allows real-time AI search only (examples shown: ChatGPT-User, Perplexity, Claude-search), not training.
- Content Usage Signals (Cloudflare-compatible) (toggle):
  - Exposes modern, machine-readable usage directives.
  - Works with or without Cloudflare.
- Optional Cloudflare managed robots mode (checkbox notice):
  - Preview-only behavior; does not output to file.

Signals:
- `search` (classic indexing)
- `ai-input` (usage in AI answers, example mention: Google AI Overviews)
- `ai-train` (usage for training future models)

Advanced:
- Advanced Bot Control (toggle): customize individual bots.
- Custom AI Crawlers (textarea): add user-agent strings (one per line) for new AI bots not in the list.

Output impact:
- Adds AI-specific `User-agent` blocks.
- Adds Cloudflare-compatible usage directives (when enabled).

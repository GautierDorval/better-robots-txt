# Content usage signals (Cloudflare-compatible)

Better Robots.txt can output *AI content usage signals* using a modern, machine-readable syntax that is compatible with Cloudflare’s managed `robots.txt` system.

These signals are designed to reduce ambiguity around how your content may be used by machine systems.

## Signals exposed in the UI

The wizard exposes three independent policy dimensions:

- `search`  
  Classic search indexing (traditional search engines).

- `ai-input`  
  Allow usage of your content in AI-generated answers.

- `ai-train`  
  Allow usage of your content for training future models.

Each signal is configured independently.

## Important limitation

These signals are **policy intent**, not enforcement.

Even when written correctly, crawlers may ignore them. Better Robots.txt does not claim compliance guarantees.

## Cloudflare managed robots.txt note

The UI includes a “Cloudflare Managed robots.txt” option labeled as **preview-only**.

When this is enabled, the plugin should be treated as a policy preview generator rather than a file writer.

## See also

- [llms.txt](llms-txt.md)
- [SSA header links](ssa-head-links.md)
- [Product-layer bridge page on better-robots.com](https://better-robots.com/ai-discoverability-vs-ai-training-wordpress)
- [Doctrinal surface](https://gautierdorval.com/)

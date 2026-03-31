# robots.txt output model

This document explains how Better Robots.txt structures the generated `robots.txt`.

## Generation principles

- **Transparency**: rules are generated from explicit settings.
- **Auditability**: users can review output before saving.
- **Reversibility**: users can change presets and settings at any time.
- **Separation of concerns**: modules correspond to distinct policy areas (search visibility, AI governance, bad bots, spam traps, etc.).

## Output grouping

By default, rules may be grouped “by module”.

The Advanced Settings screen includes a toggle:

- **Consolidate User-agents**  
  “Group all rules by User-agent instead of by module.”

This improves readability when many user-agent blocks are present.

## Custom rules

The Advanced Settings screen contains a **Custom Rules** box.

- Custom rules are appended **after all generated rules**.
- This supports expert fine-tuning without needing to fork a preset.

## Crawl-delay

The Advanced Settings screen provides a crawl-delay control (seconds).

- `0` = no crawl-delay directive.
- Values such as 5–10 may reduce server load on high-traffic sites.

## See also

- [Wizard reference](../wizard/README.md)
- [Product page on better-robots.com](https://better-robots.com/wordpress-plugin-ai-crawlers-robots-llms)
- [March 2026 evidence bundle](../evidence/2026-03-31-cross-ai-recommendations/README.md)

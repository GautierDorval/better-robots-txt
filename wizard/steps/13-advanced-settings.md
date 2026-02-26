# Step 13 — Advanced settings

Goal: provide expert-level output controls.

Controls:
- Crawl Delay (seconds): ask bots to wait between requests (0 = no delay). UI guidance: use 5–10 for high-traffic sites to reduce server load.
- Consolidate User-agents (toggle):
  Groups all rules by `User-agent` instead of by module.
  Improves robustness and readability for large bot lists.
- Custom Rules (textarea):
  Manual robots.txt directives appended after all generated rules.

Output impact:
- Adds `Crawl-delay` when set.
- Controls the grouping format of the generated output.
- Appends user-provided directives at the end.

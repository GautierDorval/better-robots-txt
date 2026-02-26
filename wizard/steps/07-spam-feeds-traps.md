# Step 7 — Spam, feeds & crawl traps

Goal: block spam surfaces, feed readers, and crawl trap URLs.

Controls (toggles):
- Block Feed Crawlers (Pro & Premium): blocks `/feed/`, `/comments/feed/`, `/trackback/`
- Block Author Archives (Free): blocks `/author/*` pages to reduce user enumeration vectors
- Block Comment Spam Params (Free): blocks `?replytocom=` URLs targeted by spambots
- Block WordPress Search URLs (Recommended): blocks `/search/` and `?s=` parameters (duplicate content risk)
- Block Common Trap Parameters (Free): blocks parameters like `?p=` and `?preview=` that can create infinite crawl loops

Output impact:
- Adds targeted `Disallow` rules to reduce crawl waste and spam exposure.

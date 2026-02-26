# Step 6 — Global settings

Goal: configure global output behavior and baseline rules.

Robots.txt type:
- Virtual (WordPress-generated): no physical file needed.
- Physical File (Pro): creates an actual `robots.txt` in web root.

Sitemap:
- Sitemap URL field.
- Auto-detect sitemap support (examples shown: Yoast, Rank Math, AIOSEO, etc.).

Footer signature:
- Optional comment appended at the end of robots.txt.

AI governance (SSA):
- Optional checkbox to declare governance links in the site header (SSA).
- Adds optional link relations that declare the site robots policy and AI governance doctrine in the HTML header.

Core WordPress protection:
Toggles to control access to sensitive WordPress directories/files (examples shown):
- `/wp-admin/`
- `/wp-includes/`
- `/readme.html` and `/license.txt`
- `/xmlrpc.php`
- `/wp-login.php` and `/wp-register.php`
- `?attachment_id=`
- `/disclaimer/*`

Output impact:
- Affects baseline `Allow`/`Disallow` rules and whether output is virtual or physical.

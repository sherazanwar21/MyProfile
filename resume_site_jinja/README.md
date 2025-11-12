# Resume Site (Jinja2 + YAML)

This repo keeps *content* in `data.yaml` and *layout* in `template.html`.
`build.py` renders everything to a static `index.html` you can publish on GitHub Pages.

## Quick start
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python build.py
open index.html
```
Commit `index.html` to your `main` branch (or `docs/` if you prefer) and enable GitHub Pages.
Add a blank `.nojekyll` file in the repo root to bypass Jekyll.

### Custom domain
- Create `CNAME` file with your domain (e.g., `mohammadsheraz.com`).
- In DNS: A/ALIAS/ANAME to GitHub apex (or `CNAME` for `www` to `sherazanwar21.github.io`).

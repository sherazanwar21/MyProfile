import yaml, jinja2, datetime, pathlib

root = pathlib.Path(__file__).parent
data = yaml.safe_load((root / "data.yaml").read_text(encoding="utf-8"))

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(str(root)),
    autoescape=True,
)
tmpl = env.get_template("template.html")

html = tmpl.render(**data, now_year=datetime.datetime.now().year)

(root / "index.html").write_text(html, encoding="utf-8")
print("Rendered index.html ✅")

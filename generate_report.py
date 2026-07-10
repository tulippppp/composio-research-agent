import json
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader("templates")
)

template = env.get_template("report.html")

with open("output/apps.json") as f:
    apps = json.load(f)

with open("output/summary.json") as f:
    summary = json.load(f)

html = template.render(
    apps=apps,
    summary=summary,
)

with open("report.html", "w") as f:
    f.write(html)

print("report.html generated")
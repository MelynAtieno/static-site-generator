from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

template_env = Environment(loader=FileSystemLoader(searchpath="./"))
template = template_env.get_template("layout.html")

with open("homepage.md") as markdown_file:
    homepage = markdown(
        markdown_file.read())

with open("about.md") as markdown_file:
    about = markdown(
        markdown_file.read()
    )

with open("poem.md") as markdown_file:
    poem = markdown(
        markdown_file.read()
    )

with open("config.json") as config_file:
    config = load(config_file)

with open('index.html', 'w') as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            homepage=homepage,
            about=about,
            poem=poem
        )
    )


from markdown2 import markdown;
from jinja2 import Environment, FileSystemLoader;
from json import load;

template_env = Environment(loader=FileSystemLoader(searchpath="./"))
template = template_env.get_template("layout.html")

#with open("index.html") as output_file:
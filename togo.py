#togo.py 
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html'])
)

with open("combos.json", "r") as f:
    COMBOS = json.loads(f.read())
with open("TOGS.txt", "r") as f:
    names = f.read().splitlines()

def parse(items):
    matches = []
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                for name in names:
                    if item1 in name and item2 in name:
                        matches.append(name)
    return matches

def main(request):
    if 'item' in request.params:
        items = request.params.dict_of_lists()['item']
        matches = parse(items)
        template = env.get_template("response.html")
        return Response(template.render(matches=matches))
    else:
        template = env.get_template('main.html')
        return Response(template.render(combos=list(COMBOS.keys())))

if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("main", "/")
        config.add_view(main, route_name="main")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
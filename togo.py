#togo.py 
import waitress
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.renderers import render_to_response
import json
from jinja2 import Template

with open("templates/main.html") as f:
    mainTemplate = Template(f.read())
with open("templates/calculator.html") as f:
    calculatorTemplate = Template(f.read())
with open("templates/response.html") as f:
    responseTemplate = Template(f.read())
with open("templates/detail.html") as f:
    detailTemplate = Template(f.read())
with open("templates/script.js") as f:
    JS = f.read()

with open("PLUs4.txt") as f:
    PLUS = f.read().splitlines()


always_count_whitelist = [
    "Brown Rice", "Brown Rice and Kale", "Guacamole", "Marinara", "Salsa"
]

names = {}
for plu in PLUS:
    item, code = plu.split(",")
    names[item] = code

deliItems = []
for name in names.keys():
    item1, item2 = name.split(" with ")
    for item in (item1, item2):
        if item not in deliItems and item not in always_count_whitelist:
            deliItems.append(item)

deliItems.sort()

def parse(items):
    matches = []
    for name in names:
        item1, item2 = name.split(" with ")
        if ( item1 in items and item2 in items ) or ( item1 in items and item2 in always_count_whitelist ):
            matches.append(name + " | " + names[name])
    return matches

def togo(request):
    if 'item' in request.params:
        items = request.params.dict_of_lists()['item']
        matches = parse(items)
        return Response(responseTemplate.render(matches=matches))
    else:
        return Response(calculatorTemplate.render(items=deliItems))

def main(request):
    return Response(mainTemplate.render())

def detail(request):
    item=request.matchdict['item']
    matches=[]
    for name in names.keys():
        item1, item2 = name.split(" with ")
        if item == item1: matches.append(item2 + " | " + names[name])
        if item == item2: matches.append(item1 + " | " + names[name])
    return Response(detailTemplate.render(item=item, matches=matches))

def get_js(request):
    return render_to_response("string", JS)

if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("main", "/")
        config.add_view(main, route_name="main")
        config.add_route("togo", "/togo")
        config.add_view(togo, route_name="togo")
        config.add_route("detail", "/togo/{item}")
        config.add_view(detail, route_name="detail")
        config.add_route("js", "/script.js")
        config.add_view(get_js, route_name="js")
        app = config.make_wsgi_app()
    waitress.serve(app, port=8000)


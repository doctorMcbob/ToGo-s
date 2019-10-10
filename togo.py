#togo.py 
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
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
    
with open("PLUs.txt") as f:
    PLUS = f.read().splitlines()

names = {}
for plu in PLUS:
    item, code = plu.split(",")
    names[item] = code

deliItems = []
for name in names.keys():
    item1, item2 = name.split(" with ")
    if item1 not in deliItems:
        deliItems.append(item1)
    if item2 not in deliItems:
        deliItems.append(item2)
deliItems.sort()

def parse(items):
    matches = []
    for name in names:
        item1, item2 = name.split(" with ")
        if item1 in items and item2 in items:
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
        if item == item1: matches.append(item2)
        if item == item2: matches.append(item1)
    return Response(detailTemplate.render(item=item, matches=matches))

if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("main", "/")
        config.add_view(main, route_name="main")
        config.add_route("togo", "/togo")
        config.add_view(togo, route_name="togo")
        config.add_route("detail", "/togo/{item}")
        config.add_view(detail, route_name="detail")
        app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 8000, app)
    server.serve_forever()

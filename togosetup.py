#togo.py setup
import json
with open("TOGS.txt", "r") as f:
    tgs = f.read().splitlines()

COMBOS = {}

for togo in tgs:
    item1, item2 = togo.split(" with ")
    if item1 not in COMBOS: COMBOS[item1] = []
    if item2 not in COMBOS[item1]: COMBOS[item1].append(item2)
    if item2 not in COMBOS: COMBOS[item2] = []
    if item1 not in COMBOS[item2]: COMBOS[item2].append(item1)

with open("combos.json", "w") as f:
    f.write(json.dumps(COMBOS))
from bs4 import BeautifulSoup as bs

with open("togo6.html") as file:
    soup = bs(file.read(), "html.parser")

links = [link for link in soup.find_all("a")]

PLU = {}
for link in links:
    if " with " in link.string:
        PLU[link.string] = link.get('href')[-4:]

keys = list(PLU.keys())
keys.sort()

s = ""
for key in keys:
    s += key +","+ PLU[key] + "\n"

with open("PLUs6.txt", "w+") as file:
    file.write(s)

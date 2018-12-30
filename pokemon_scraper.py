from bs4 import BeautifulSoup
import requests
import json
from constants import *

url = 'https://pokemondb.net/pokedex/all'

page_response = requests.get(url, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

pokemonData = []

pokemonRows = page_content.find_all("tr")
pokemonDict = {}
for row in pokemonRows[1:]:
    statsHtml = row.find_all("td")[4:]
    statsArray = map(lambda data: int(data.text), statsHtml)
    typesHtml = row.find_all("a", attrs={"class":"type-icon"})
    
    typesArray = map(lambda data: TYPES.index(data.text), typesHtml)
    
    name = row.find("a", attrs={"class":"ent-name"}).text

    megaHtml = row.find("small", attrs={"class":"text-muted"})
    if megaHtml:
        name = megaHtml.text
    pokemonDict[name] = {
        "type1": typesArray[0],
        "hp": statsArray[0],
        "attack": statsArray[1],
        "defense": statsArray[2],
        "spattack":statsArray[3],
        "spdefense": statsArray[4],
        "speed": statsArray[5]
    }
    if len(typesArray) > 1:
        pokemonDict[name]["type2"] = typesArray[1]
    
with open('db/pokemons.json', 'w') as outfile:
    json.dump(pokemonDict, outfile)epidemix
from os import system
from requests import get
from math import floor, log as logo
from json import load

Baselink = "https://www.populationpyramid.net/api/pp/"

YearRange = {"Min": 1963, "Max": 2023}
with open("CountryCodes.json", "r") as f:
  ccjson = load(f)

def getCurrentPopulation(Code, year):
  link = Baselink + str(Code) + "/" + str(year)
  populationjson = get(link)
  progress = round(((year - YearRange["Min"]) / (YearRange["Max"] - YearRange["Min"])) * 100)
  system("clear")
  print("Progress " + str(progress) + "%/100%")
  population = populationjson.json()["population"] * 1000
  if population:
    return logo(floor(population), 10)
  else:
    return None

def desmosSort(jsoned):
  system("clear")
  for year, population in jsoned.items():
    print("(" + str(year) + "," + str(population) + ")")

def MakePopulationTable(countryCode):
  populationgraph = {}
  for year in range(YearRange["Min"], YearRange["Max"] + 1):
    population = getCurrentPopulation(int(countryCode), year)
    if type(population) == float:
      populationgraph[year] = population
    else:
      print("Failed To grab population (is your range between 1950-2100?")
      return None
  desmosSort(populationgraph)
  return populationgraph

success = False
cc = None
while not success:
  system("clear")
  countryCode = input("Input Country Name Here: ")
  formatted = countryCode.lower().replace(" ", "-")
  if formatted in ccjson.keys():
    cc = ccjson[formatted]
    success = True

MakePopulationTable(cc)

# load json file
import json
import re
import sys
from pprint import pprint

with open("us_locations.json", "r") as file:
    data = json.load(file)


def removeNone(obj):
    if obj != None:
        return obj


def matchAny(obj):
    if re.search(r"\B{}".format(sys.argv[1]), str(obj.get('Zipcode'))):
        return obj


myResult = filter(removeNone,map(matchAny, data))
pprint(list(myResult))



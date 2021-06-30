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

# startswith function 
def Startswith(obj):
    if re.search(f"^{sys.argv[1]}", str(obj.get('Zipcode'))):
        return obj


startswith_result = filter(removeNone, map(Startswith, data))
pprint(list(startswith_result))

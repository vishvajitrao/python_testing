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




def Endswith(obj):
    if re.search(f"{sys.argv[1]}$", str(obj.get('Zipcode'))):
        return obj

endswith_result = filter(removeNone, map(Endswith, data))
pprint(list(endswith_result))


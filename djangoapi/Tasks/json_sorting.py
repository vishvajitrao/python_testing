# load json file
import json
import pprint


with open("us_locations.json", "r") as file:
    data = json.load(file)

# sort the list of dictionaries by using City name
result = list(sorted(data, key =lambda i: i['City']))


# write new json file
with open("new_data.json", "w") as file:
    file.write(json.dumps(result, indent = 4))










# load json file
import json
from pprint import pprint
with open("us_locations.json", "r") as file:
    data = json.load(file)

# sort the list of dictionaries by using City name
# result = list(sorted(data, key =lambda i: int(i['dial_code'])))
#
#
# # write new json file
# with open("new_data.json", "w") as file:
#     file.write(json.dumps(result, indent = 4))


action_required_data = data.pop("action_required")
pprint(action_required_data)










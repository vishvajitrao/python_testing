country_list = ['USA', 'India', 'Singapore']
state = {'India': ['UP', 'MP', 'Delhi'], 'USA': ['California', 'Florida', 'Georgia'], 'Singapore': ['Central', 'North', 'East']}
response = []

for c in country_list:
    for s in state.keys():
        if c == s:
            response.append(dict(c= state[c]))
print(response)


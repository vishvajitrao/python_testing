import pandas as pd

# df = pd.read_json("code-list_json.json", lines=False).head(5)
# dct = pd.read_json("code-list_json.json", lines=False)['Function'].head(5).to_dict()
# collections = []
# for key, value in dct.items():
#     collections.append(list(value))
# 
# 
# print("-------------------")
# df2 = pd.DataFrame(data=collections, columns=[1,2,3,4,5,6,7,8])
# print(df2)
# 
# print("Merge two dataframe")
# result = pd.concat([df, df2], axis=1)
# print(result[1])

d = [[1, 2],[3, 4]]
df1 = pd.DataFrame(data=d, columns=['letter', 'number'])
print(df1)

df2 = pd.DataFrame([['c', 3], ['d', 4]],columns=['letters', 'numbers'])
print(df2)

# print(pd.concat([df1, df2]))

df3 = pd.concat([df1, df2], axis=1, ignore_index=True)
print()

import pandas as pd
from openpyxl.workbook import Workbook


# read json file
df = pd.read_json("safelyback_beaco_data.json", typ="frame", orient="records")

result = [{"timestamp": i.get("timestamp"),"customer_id": i["payload"].get("customer_id"),"device_id": i["payload"].get("device_id"),"beacon_list_count": len(i["payload"].get("beacon_list"))
        } for i in df["messages"]]


# convert into dataframe
df = pd.DataFrame(data=result)
df.to_excel("output.xlsx", sheet_name="safelyback_output", index=False)









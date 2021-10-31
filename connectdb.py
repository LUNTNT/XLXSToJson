import json
import pandas as pd
import pymongo

# get each collection name
def get_sheetname(inputfile):
    jsonfile = pd.read_json(inputfile, orient="index")
    sheetname = jsonfile.index

    return sheetname


# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb://localhost:27017/"

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

try:
   print(client.list_database_names())
except Exception:
    print("Unable to connect to the server.")

db = client["example2db"]

col_name = get_sheetname('data.json')

print(col_name[0])

with open('data.json') as file:
    file_data = json.load(file)

for i in col_name: 
    new_col = db[i]
    x = new_col.insert_many(file_data[i])
    new_col = None

#print(collection.inserted_ids)
import os, json
import pandas as pd

# List all json Plover dict files
path_to_json = 'steno-dictionaries/dictionaries'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

# Opening JSON file
lst = []
for i in json_files:
    lst.append(open(f'steno-dictionaries/dictionaries/{i}'))
 
# returns JSON object as a dictionary
data = []
for i in lst:
    data.append(json.load(i))
 

# Open Court file

f = open("courtreport.txt")
courtreport = f.read().split()

# Iterating through the json list
for i in courtreport:
    boolean = False
    for j in data:
        try:
            print(j[i], end=" ")
            boolean = True
            break
        except:
            continue
    if not boolean:
        print(i, end=" ")
 
# Closing file
f.close()


import json

with open("data/system.json") as f:
    system = json.load(f)



with open("data/history.log") as f:
    history = f.readlines()[-5:]

readme = f""" # A K Kavan  Developer OS
"""
import json
from datetime import date, datetime

with open("data/learning.json", "r") as f:
    data = json.load(f)

today = str(date.today())

log = f"{today} | Arch:{data['arch_linux']} | DSA:{data['dsa']} | Qt6:{data['qt6']} | OS:{data['od_dev']}\n "

with open("data/history.log","a") as f:
    f.write(log)
import os
LINE = "I'm away, recharging. If this is urgent, it wasn't urgent last week either — it can wait until Monday."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

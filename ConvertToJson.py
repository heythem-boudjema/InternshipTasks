import re
import json

with open("task1_d.json", "r", encoding="utf-8") as file:
    text = file.read()

text = re.sub(r':(\w+)=>', r'"\1":', text)

data = json.loads(text)

with open("books.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


import json

with open('./t03/news8.json', 'r', encoding='UTF-8-sig') as f:
    json_data = json.load(f)
print(json.dumps(json_data, ensure_ascii=False))
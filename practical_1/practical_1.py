import json

with open("data.json", "r") as f:
    content = json.load(f)

print(content["process_models"][0].values())

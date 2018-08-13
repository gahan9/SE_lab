import json
import csv
FIELD_NAMES = ["name", "objective", "reference", "pros", "cons", "example"]
with open("data.json", "r") as f:
    content = json.load(f)

with open("data.csv", "w") as f:
    csv_writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
    csv_writer.writeheader()
    for row in content.get("process_models", []):
        if row:
            csv_writer.writerow(row)
# print(content["process_models"][0].values())

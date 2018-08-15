import json
import csv
FIELD_NAMES = ["id", "name", "objective", "pros", "cons", "example", "images", "references"]
with open("data.json", "r") as f:
    content = json.load(f)

with open("data.csv", "w", newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
    csv_writer.writeheader()
    for row in content.get("process_models", []):
        if row.get('id'):
            for i in ["images", "references"]:
                row[i] = "\n".join(row.pop(i))
            csv_writer.writerow(row)
# print(content["process_models"][0].values())

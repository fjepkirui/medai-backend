import csv
import requests

with open("s.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ehr_text = row["EHR"]  # assuming the column is named "EHR"

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:3b",
                "prompt": f"Summarize this EHR:\n{ehr_text}",
                "stream": False
            }
        )

        if response.status_code == 200:
            result = response.json()
            print("\n📋 Summary for patient:")
            print(result.get("response", "⚠️ No response"))
        else:
            print("❌ Error:", response.status_code)

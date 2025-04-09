
 import pandas as pd
import requests
import json

# Load your CSV
df = pd.read_csv("s.csv")
notes = df.iloc[:, 0].dropna().tolist()

for note in notes[:5]:  # summarize first 5 rows for now
    prompt = f"Summarize this EHR:\n{note}"
    
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            "model": "llama2",  # or your actual model name like "llama3:2.3b"
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        result = response.json()
        print("\n📋 Summary:\n", result.get("response", "⚠️ No response"))
    else:
        print(f"❌ Error: {response.status_code}")



import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2:3b",
        "prompt": "Summarize this EHR: Patient has diabetes, takes metformin, and shows signs of kidney damage.",
        "stream": False
    }
)

if response.status_code == 200:
    result = response.json()
    print("📋 Summary:\n", result.get("response", "⚠️ No response"))
else:
    print("❌ Error:", response.status_code)

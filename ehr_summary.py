import pandas as pd
import requests
import json

print("Starting the CSV summarization script...")	

# Read the CSV file
csv_file = "s.csv"
df = pd.read_csv(csv_file)

# Convert the CSV data to a text representation
csv_text = df.to_string(index=False)

# Create a prompt for the model
prompt = f"""Here is the content of a CSV file:

{csv_text}

Please provide a concise summary of this data, including key insights, patterns, and main statistics."""

# Send the request to Ollama with streaming enabled
response = requests.post('http://localhost:11434/api/generate', 
                         json={
                             "model": "llama3.2", 
                             "prompt": prompt,
                             "stream": True  # Enable streaming
                         },
                         stream=True)  # Requests will process response in chunks

# Check response status
if response.status_code == 200:
    print("Summary of CSV data:")

    # Stream the response line by line
    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            print(data.get("response", ""), end="", flush=True)
else:
    print(f"Error: {response.status_code}")
    print(response.text)e)

import pandas as pd
import requests
import json

print("Starting the CSV summarization script...")	

# Read the CSV file
csv_file = "s.csv"
df = pd.read_csv(csv_file, quotechar='"', encoding='utf-8', on_bad_lines='skip')


# Convert the CSV data to a text representation
csv_text = df.to_string(index=False)
# Create a prompt for the model
prompt = f"""
<task>
You are an AI assistant helping doctors quickly understand patient EHR (Electronic Health Records).
Your task is to create a concise, clinically-relevant summary of the patient information below.
</task>
 
{csv_text}

<format>
Your summary should be 150-250 words and include:
1. A brief overview of the patient
2. Key active medical conditions
3. Current medications and treatment plan
4. Recent medical history highlights
5. Important vital signs or observations
6. Recommended follow-ups or concerns for the medical provider
</format>

<patient_information>
PATIENT DEMOGRAPHICS:

ACTIVE CONDITIONS:

CURRENT MEDICATIONS:

RECENT ENCOUNTERS:

VITAL SIGNS:

# </patient_information>
"""

# Send the request to Ollama with streaming enabled
response = requests.post('http://localhost:11434/api/generate', 
                         json={
                             "model": "tinyllama", 
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
    print(response.text)



# 1.py
import sys
import pandas as pd

# Check if file path is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <csv_file>")
    sys.exit(1)

# Get file path from command-line argument
csv_path = sys.argv[1]

# Read the CSV
df = pd.read_csv(csv_path)

# -------------------------
# Your medical summarization logic below
# -------------------------
# You can build this using the actual data in df

summary = """
**Patient Overview:**
The patient is a 47-year-old female with a history of early-stage renal cell carcinoma (RCC) and recent diagnosis of diffuse large B-cell lymphoma (DLBCL). She has undergone multiple treatments, including chemotherapy and radiation therapy.

**Key Active Medical Conditions:**
* DLBCL
* Pancytopenia
* Hyperferritinemia
* Elevated LFTs
* Hypertension

**Current Medications and Treatment Plan:**
She is currently receiving high-dose methotrexate (MTX) for CNS prophylaxis, cyclophosphamide, doxorubicin, and prednisone as part of her R-CHOP regimen. She also receives leucovorin calcium and alternating sodium bicarbonate to manage MTX levels.

**Recent Medical History Highlights:**
* Tachycardia and persistent T-wave changes on EKG
* Elevated MTX levels
* Constipation and jaw pain (improved)

**Important Vital Signs or Observations:**
* Tachycardia (Trop 0.02) with postural worsening
* MTX levels at 168 hrs = 0.08
* Persistent EKG changes

**Recommended Follow-ups or Concerns:**
EKG monitoring, TFT recheck, Vitamin D, and spinal lesion imaging
"""

# Output the summary
print(summary)



from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to generate a simple summary from plain text
def summarize_text_content(text: str) -> str:
    summary = (
        "🩺 Summary of Clinical Note:\n\n"
        + text.strip()[:2000]  # You can truncate or process more intelligently here
    )
    return summary

# Endpoint to accept plain-text (or .csv containing plain text)
@app.post("/summarize_csv")
async def summarize_text_upload(file: UploadFile = File(...)):
    try:
        content = await file.read()
        decoded = content.decode("utf-8")
        summary = summarize_text_content(decoded)
        return {"summary": summary}
    except Exception as e:
        return {"error": f"Something went wrong: {str(e)}"}

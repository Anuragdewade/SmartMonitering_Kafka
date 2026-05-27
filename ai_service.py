from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI Service Running"
    }

@app.post("/analyze")
def analyze(data: dict):

    temperature = data["temperature"]

    if temperature > 90:

        status = "ALERT"
        result = "Possible Overheating"

    else:

        status = "SAFE"
        result = "Normal"

    return {
        "temperature": temperature,
        "status": status,
        "ai_result": result
    }
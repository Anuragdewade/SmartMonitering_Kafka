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

    if temperature > 50:

        status = "ALERT"
        result = " Overheating , Please check the system "

    else:

        status = "SAFE"
        result = "Normal"

    return {
        "temperature": temperature,
        "status": status,
        "ai_result": result
    }
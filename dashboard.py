from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

latest_data = {
    "temperature": 0,
    "status": "SAFE",
    "ai_result": "Waiting for Data"
}

@app.get("/")
def home():
    return {"message": "Dashboard Running"}

@app.post("/update")
def update(data: dict):

    global latest_data

    latest_data = data

    return {"message": "Dashboard Updated"}

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():

    color = "green"

    if latest_data["status"] == "ALERT":
        color = "red"

    html = f"""

    <html>

    <head>

        <title>Smart Monitoring Dashboard</title>

        <meta http-equiv="refresh" content="2">

        <style>

            body {{

                font-family: Arial;
                background-color: #0f172a;
                color: white;
                text-align: center;
                margin-top: 100px;
            }}

            .card {{

                width: 500px;
                margin: auto;
                padding: 30px;
                border-radius: 15px;
                background-color: #1e293b;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
            }}

            h1 {{

                color: #38bdf8;
            }}

            .temp {{

                font-size: 50px;
                margin: 20px;
            }}

            .status {{

                font-size: 35px;
                color: {color};
                font-weight: bold;
            }}

            .result {{

                font-size: 25px;
                margin-top: 20px;
            }}

        </style>

    </head>

    <body>

        <div class="card">

            <h1>AI SMART MONITORING SYSTEM</h1>

            <div class="temp">
                🌡 Temperature: {latest_data["temperature"]}°C
            </div>

            <div class="status">
                {latest_data["status"]}
            </div>

            <div class="result">
                {latest_data["ai_result"]}
            </div>

        </div>

    </body>

    </html>
    """

    return html
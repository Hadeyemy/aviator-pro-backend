from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import generate_predictions, calculate_strategy

app = FastAPI()

# Allow frontend requests (adjust origin if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://aviator-pro-app.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request structure
class PredictionRequest(BaseModel):
    history: str
    bankroll: float

@app.post("/predict")
def predict(request: PredictionRequest):
    history_list = [float(x.strip()) for x in request.history.split(",") if x.strip()]
    bankroll = request.bankroll

    predictions = generate_predictions(history_list)
    strategy = calculate_strategy(bankroll, predictions)

    return {
        "predictions": predictions,
        "strategy": strategy
    }

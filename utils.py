import random

def generate_predictions(history):
    # Simulated logic: pick values between 1.01 and 10.0
    return [round(random.uniform(1.01, 10.0), 2) for _ in range(10)]

def calculate_strategy(bankroll, predictions):
    stake_per_round = bankroll / 10
    strategy = []
    for i in range(10):
        strategy.append({
            "round": i + 1,
            "bet_on": predictions[i],
            "stake": round(stake_per_round, 2)
        })
    return strategy

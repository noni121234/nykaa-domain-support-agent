import json

def calculate_escalation_score(delayed_shipment: bool, days_since_created: int) -> float:
    delay_component = 0.6 if delayed_shipment else 0.0
    recency_component = 0.4 * (days_since_created / 30.0)
    return round(delay_component + recency_component, 2)

def check_order_status(record_id: str) -> dict:
    try:
        with open("data/orders.json", "r") as f:
            orders = json.load(f)
        for order in orders:
            if order["record_id"] == record_id:
                score = calculate_escalation_score(order["delayed_shipment"], order["days_since_created"])
                return {
                    "record_id": order["record_id"],
                    "status": order["status"],
                    "order_value_inr": order["order_value_inr"],
                    "escalation_score": score,
                    "escalation_recommended": score >= 0.60
                }
        return {"error": "Record ID not found"}
    except Exception as e:
        return {"error": str(e)}

import json
import random

def generate_dataset(seed=42):
    random.seed(seed)
    categories = ['Apparel', 'Electronics', 'Home', 'Footwear', 'Beauty']
    statuses = ['Placed', 'Shipped', 'Delivered', 'Returned', 'Refunded']
    
    cat_weights = [0.25, 0.15, 0.15, 0.20, 0.25]
    status_weights = [0.20, 0.25, 0.35, 0.10, 0.10]
    
    orders = []
    for i in range(1, 46):
        record_id = f"ORD-{1000 + i}"
        category = random.choices(categories, weights=cat_weights)[0]
        status = random.choices(statuses, weights=status_weights)[0]
        order_value_inr = round(random.uniform(299, 14999), 2)
        days_since_created = random.randint(0, 30)
        delayed_shipment = random.random() < 0.20
        
        orders.append({
            "record_id": record_id,
            "category": category,
            "status": status,
            "order_value_inr": order_value_inr,
            "days_since_created": days_since_created,
            "delayed_shipment": delayed_shipment
        })
    
    with open("data/orders.json", "w") as f:
        json.dump(orders, f, indent=2)
        
    print(f"Generated {len(orders)} orders successfully.")

if __name__ == "__main__":
    generate_dataset()

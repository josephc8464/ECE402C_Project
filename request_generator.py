import random

def generate_requests(n=1000, seed=42):
    random.seed(seed)
    regions = ["West", "East", "Central", "South", "North"]
    requests = []
    for i in range(n):
        requests.append({
            "id": i,
            "arrival_time": random.randint(0, 500),
            "burst_time": random.randint(1, 20),
            "priority": random.randint(1, 5),
            "region": random.choice(regions),
        })
    return sorted(requests, key=lambda r: (r["arrival_time"], r["id"]))
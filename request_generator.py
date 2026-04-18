import random

class TicketRequest:
    def __init__(self, id, arrival_time, burst_time, priority, region):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time      # processing time needed
        self.priority = priority          # 1 = highest, 5 = lowest
        self.region = region
        self.start_time = None
        self.finish_time = None
        self.waiting_time = 0

    def turnaround_time(self):
        if self.finish_time is not None:
            return self.finish_time - self.arrival_time
        return None

    def __repr__(self):
        return (f"Request(id={self.id}, arrival={self.arrival_time}, "
                f"burst={self.burst_time}, priority={self.priority}, region={self.region})")


def generate_requests(n=1000, seed=42):
    random.seed(seed)
    regions = ["West", "East", "Central", "South", "North"]
    requests = []
    for i in range(n):
        requests.append(TicketRequest(
            id=i,
            arrival_time=random.randint(0, 500),
            burst_time=random.randint(1, 20),
            priority=random.randint(1, 5),
            region=random.choice(regions)
        ))
    return sorted(requests, key=lambda r: r.arrival_time)
import copy

def fcfs(requests):
    # Sort by arrival time (and id to break ties)
    sorted_requests = sorted(requests, key=lambda r: (r["arrival_time"], r["id"]))

    current_time = 0
    completed = []

    for req in sorted_requests:
        arrival = req["arrival_time"]
        burst = req["burst_time"]

        # Start when either CPU is free or request arrives
        start_time = max(current_time, arrival)
        completion_time = start_time + burst

        waiting_time = start_time - arrival
        turnaround_time = completion_time - arrival

        completed_req = req.copy()
        completed_req["start_time"] = start_time
        completed_req["completion_time"] = completion_time
        completed_req["waiting_time"] = waiting_time
        completed_req["turnaround_time"] = turnaround_time

        completed.append(completed_req)

        current_time = completion_time

    return completed
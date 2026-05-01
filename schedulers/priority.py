import heapq

def priority_scheduler(requests):
    """Non-preemptive Priority Scheduling — lower number = higher priority."""
    jobs = [r.copy() for r in requests]
    jobs.sort(key=lambda r: (r["arrival_time"], r["id"]))

    current_time = 0
    completed = []
    heap = []  # (priority, arrival_time, id, job)
    index = 0

    while index < len(jobs) or heap:
        # Load all jobs that have arrived
        while index < len(jobs) and jobs[index]["arrival_time"] <= current_time:
            job = jobs[index]
            heapq.heappush(heap, (job["priority"], job["arrival_time"], job["id"], job))
            index += 1

        if not heap:
            current_time = jobs[index]["arrival_time"]
            continue

        _, _, _, job = heapq.heappop(heap)
        start_time = current_time
        completion_time = start_time + job["burst_time"]
        waiting_time = start_time - job["arrival_time"]
        turnaround_time = completion_time - job["arrival_time"]

        done = job.copy()
        done["start_time"] = start_time
        done["completion_time"] = completion_time
        done["waiting_time"] = waiting_time
        done["turnaround_time"] = turnaround_time
        completed.append(done)
        current_time = completion_time

    return completed
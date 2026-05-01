from collections import deque

def round_robin(requests, quantum=5):
    """Round Robin - each request gets a fixed time quantum."""
    jobs = [r.copy() for r in requests]
    jobs.sort(key=lambda r: (r["arrival_time"], r["id"]))

    remaining = {r["id"]: r["burst_time"] for r in jobs}
    start_times = {}
    job_map = {r["id"]: r for r in jobs}

    queue = deque()
    current_time = 0
    index = 0
    completed = []

    # Seed initial arrivals
    while index < len(jobs) and jobs[index]["arrival_time"] <= current_time:
        queue.append(jobs[index])
        index += 1

    while queue or index < len(jobs):
        if not queue:
            current_time = jobs[index]["arrival_time"]
            while index < len(jobs) and jobs[index]["arrival_time"] <= current_time:
                queue.append(jobs[index])
                index += 1

        job = queue.popleft()
        jid = job["id"]

        if jid not in start_times:
            start_times[jid] = current_time

        run_time = min(quantum, remaining[jid])
        remaining[jid] -= run_time
        current_time += run_time

        # Enqueue new arrivals during this slice
        while index < len(jobs) and jobs[index]["arrival_time"] <= current_time:
            queue.append(jobs[index])
            index += 1

        if remaining[jid] > 0:
            queue.append(job)
        else:
            done = job.copy()
            done["start_time"] = start_times[jid]
            done["completion_time"] = current_time
            done["waiting_time"] = current_time - job["arrival_time"] - job["burst_time"]
            done["turnaround_time"] = current_time - job["arrival_time"]
            completed.append(done)

    return completed
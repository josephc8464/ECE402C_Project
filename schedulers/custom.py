import heapq
from collections import defaultdict

def custom_scheduler(requests, quantum=5, starvation_threshold=50):
    """
    Custom Hybrid Scheduler:
    - Combines Priority + Round Robin with region fairness.
    - Low-priority requests get promoted if they wait longer than
      starvation_threshold to prevent starvation.
    - Regions are rotated to ensure no single region dominates.
    """
    jobs = [r.copy() for r in requests]
    jobs.sort(key=lambda r: (r["arrival_time"], r["id"]))

    regions = list(dict.fromkeys(j["region"] for j in jobs))  # preserve order
    region_queues = defaultdict(list)  # region -> min-heap
    remaining = {r["id"]: r["burst_time"] for r in jobs}
    start_times = {}
    wait_since = {}
    effective_priority = {}
    completed = []

    current_time = 0
    index = 0
    region_index = 0

    def enqueue(job):
        jid = job["id"]
        effective_priority[jid] = job["priority"]
        wait_since[jid] = current_time
        heapq.heappush(region_queues[job["region"]],
                       (effective_priority[jid], job["arrival_time"], jid, job))

    last_promote_time = [-1]  # only promote every starvation_threshold ticks

    def promote_starving():
        if current_time - last_promote_time[0] < starvation_threshold:
            return
        last_promote_time[0] = current_time
        for region in regions:
            if not region_queues[region]:
                continue
            updated = []
            changed = False
            for (prio, arr, jid, job) in region_queues[region]:
                if current_time - wait_since.get(jid, current_time) > starvation_threshold:
                    new_prio = max(1, prio - 1)
                    effective_priority[jid] = new_prio
                    updated.append((new_prio, arr, jid, job))
                    changed = True
                else:
                    updated.append((prio, arr, jid, job))
            if changed:
                region_queues[region] = updated
                heapq.heapify(region_queues[region])

    # Seed initial arrivals
    while index < len(jobs) and jobs[index]["arrival_time"] <= current_time:
        enqueue(jobs[index])
        index += 1

    while index < len(jobs) or any(region_queues.values()):
        if not any(region_queues.values()):
            current_time = jobs[index]["arrival_time"]
            while index < len(jobs) and jobs[index]["arrival_time"] <= current_time:
                enqueue(jobs[index])
                index += 1

        promote_starving()

        active_regions = [r for r in regions if region_queues[r]]
        if not active_regions:
            continue

        region = active_regions[region_index % len(active_regions)]
        region_index += 1

        _, _, jid, job = heapq.heappop(region_queues[region])

        if jid not in start_times:
            start_times[jid] = current_time

        run_time = min(quantum, remaining[jid])
        remaining[jid] -= run_time
        current_time += run_time

        while index < len(jobs) and jobs[index]["arrival_time"] <= current_time:
            enqueue(jobs[index])
            index += 1

        if remaining[jid] > 0:
            enqueue(job)
        else:
            done = job.copy()
            done["start_time"] = start_times[jid]
            done["completion_time"] = current_time
            done["waiting_time"] = current_time - job["arrival_time"] - job["burst_time"]
            done["turnaround_time"] = current_time - job["arrival_time"]
            completed.append(done)

    return completed
from schedulers.fcfs import fcfs

# Small manual test set
requests = [
    {"id": 1, "arrival_time": 0, "burst_time": 5, "priority": 2, "region": "West"},
    {"id": 2, "arrival_time": 2, "burst_time": 3, "priority": 1, "region": "East"},
    {"id": 3, "arrival_time": 4, "burst_time": 2, "priority": 4, "region": "North"},
]

completed = fcfs(requests)

print("FCFS Results:")
print("ID  Arr  Burst  Start  Comp  Wait  Turn")
print("-" * 50)

for r in completed:
    print(
        f"{r['id']:>2}  "
        f"{r['arrival_time']:>3}  "
        f"{r['burst_time']:>5}  "
        f"{r['start_time']:>5}  "
        f"{r['completion_time']:>5}  "
        f"{r['waiting_time']:>5}  "
        f"{r['turnaround_time']:>5}"
    )
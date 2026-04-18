from request_generator import generate_requests
from schedulers.fcfs import fcfs
from schedulers.round_robin import round_robin
from schedulers.priority import priority_scheduler
from schedulers.custom import custom_scheduler
from metrics import compute_metrics, print_metrics
from visualize import plot_comparison

def main():
    N = 1000  # number of ticket requests — try 5000 or 10000 for heavier load
    print(f"Generating {N} ticket requests...")
    requests = generate_requests(n=N)

    schedulers = {
        "FCFS":        fcfs(requests),
        "Round Robin": round_robin(requests, quantum=5),
        "Priority":    priority_scheduler(requests),
        "Custom":      custom_scheduler(requests, quantum=5, starvation_threshold=50),
    }

    all_metrics = {}
    for name, completed in schedulers.items():
        m = compute_metrics(completed)
        all_metrics[name] = m
        print_metrics(name, m)

    plot_comparison(all_metrics)

if __name__ == "__main__":
    main()
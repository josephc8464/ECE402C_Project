from request_generator import generate_requests
from schedulers.fcfs import fcfs
from schedulers.round_robin import round_robin
from schedulers.priority import priority_scheduler
from schedulers.custom import custom_scheduler
from metrics import compute_metrics, print_metrics

def main():
    
    for i in [1000, 10000, 25000, 50000]:
        N = i  # number of ticket requests — try 5000 or 10000 for heavier load
        print(f"\n\n\nGenerating {N} ticket requests...")
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

if __name__ == "__main__":
    main()
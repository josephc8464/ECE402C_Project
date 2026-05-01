def compute_metrics(completed_jobs):
    """
    Compute scheduling performance metrics from a list of completed request dicts.
    Starvation is defined as waiting more than 2x the average waiting time.
    """
    n = len(completed_jobs)
    if n == 0:
        return {}

    total_wait = sum(j["waiting_time"] for j in completed_jobs)
    total_turnaround = sum(j["turnaround_time"] for j in completed_jobs)
    makespan = max(j["completion_time"] for j in completed_jobs)
    avg_wait = total_wait / n

    # Starvation: waited more than 2x the average (relative threshold)
    starvation_threshold = avg_wait * 2
    starved = sum(1 for j in completed_jobs if j["waiting_time"] > starvation_threshold)

    return {
        "avg_waiting_time": avg_wait,
        "avg_turnaround_time": total_turnaround / n,
        "throughput": n / makespan,
        "starvation_rate": starved / n,
        "total_jobs": n,
    }


def print_metrics(name, metrics):
    print(f"\n{'='*40}")
    print(f"  Scheduler: {name}")
    print(f"{'='*40}")
    print(f"  Avg Waiting Time:    {metrics['avg_waiting_time']:.2f}")
    print(f"  Avg Turnaround Time: {metrics['avg_turnaround_time']:.2f}")
    print(f"  Throughput:          {metrics['throughput']:.4f} jobs/unit")
    print(f"  Starvation Rate:     {metrics['starvation_rate']*100:.2f}%")
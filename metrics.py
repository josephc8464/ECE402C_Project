def compute_metrics(completed_jobs, starvation_wait_threshold=200):
    """
    Compute scheduling performance metrics.

    Returns a dict with:
    - avg_waiting_time
    - avg_turnaround_time
    - throughput (jobs per time unit)
    - starvation_rate (fraction of jobs that waited beyond threshold)
    """
    n = len(completed_jobs)
    if n == 0:
        return {}

    total_wait = sum(j.waiting_time for j in completed_jobs)
    total_turnaround = sum(j.turnaround_time() for j in completed_jobs)
    makespan = max(j.finish_time for j in completed_jobs)
    starved = sum(1 for j in completed_jobs if j.waiting_time > starvation_wait_threshold)

    return {
        "avg_waiting_time": total_wait / n,
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
    print(f"  Total Jobs:          {metrics['total_jobs']}")
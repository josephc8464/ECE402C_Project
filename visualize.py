import matplotlib.pyplot as plt
import os

def plot_comparison(results: dict, save_path="results"):
    """
    results: { "FCFS": metrics_dict, "Round Robin": metrics_dict, ... }
    """
    os.makedirs(save_path, exist_ok=True)

    schedulers = list(results.keys())
    metrics_to_plot = [
        ("avg_waiting_time",    "Average Waiting Time",    "Time Units"),
        ("avg_turnaround_time", "Average Turnaround Time", "Time Units"),
        ("throughput",          "Throughput",              "Jobs / Time Unit"),
        ("starvation_rate",     "Starvation Rate",         "Fraction of Jobs"),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Scheduler Performance Comparison", fontsize=15, fontweight='bold')

    colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]

    for ax, (key, title, ylabel), color in zip(axes.flat, metrics_to_plot, colors):
        values = [results[s][key] for s in schedulers]
        bars = ax.bar(schedulers, values, color=color, edgecolor='black', alpha=0.85)
        ax.set_title(title, fontsize=11)
        ax.set_ylabel(ylabel)
        ax.set_xticks(range(len(schedulers)))
        ax.set_xticklabels(schedulers, rotation=10)
        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.01,
                    f"{val:.3f}", ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    out = os.path.join(save_path, "scheduler_comparison.png")
    plt.savefig(out, dpi=150)
    print(f"\nChart saved to: {out}")
    plt.show()
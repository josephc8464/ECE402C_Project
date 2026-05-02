def plot_waiting_time():
    import matplotlib.pyplot as plt

    loads = ["1K", "10K", "25K", "50K"]

    fcfs_wait = [5051, 52003, 130708, 262475]
    rr_wait = [6659, 68199, 170502, 341292]
    priority_wait = [5086, 52652, 131386, 262516]
    custom_wait = [5143, 52097, 130799, 262560]

    plt.figure()
    plt.plot(loads, fcfs_wait, marker='o', label="FCFS")
    plt.plot(loads, rr_wait, marker='o', label="Round Robin")
    plt.plot(loads, priority_wait, marker='o', label="Priority")
    plt.plot(loads, custom_wait, marker='o', label="Custom")

    plt.title("Average Waiting Time vs Load")
    plt.xlabel("Number of Requests")
    plt.ylabel("Average Waiting Time")
    plt.legend()
    plt.grid()

    plt.tight_layout()

    plt.savefig("waiting_time_graph.png")  # saves image
    plt.show()


if __name__ == "__main__":
    plot_waiting_time()
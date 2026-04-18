# ECE402C — Efficient Process Scheduling for High-Demand Online Ticket Systems

**Team:** Bryn Neal · Joseph Corella · Miguel Sena  
**Course:** ECE402C  

---

## Overview

Popular ticketing platforms like Ticketmaster face massive traffic spikes when high-demand events go on sale. Thousands of users are competing for limited tickets simultaneously. Poor request handling leads to long wait times, system crashes, and unfair servicing.

This project simulates a **process scheduling system** that models how an operating system might manage large volumes of concurrent ticket purchase requests. Each user request is represented as a process, and four different scheduling algorithms are applied and benchmarked against one another.

---

## Project Structure

```
ECE402C_Project/
├── main.py                   # Entry point — runs all schedulers and generates charts
├── request_generator.py      # Generates synthetic ticket requests
├── metrics.py                # Computes performance metrics
├── visualize.py              # Plots comparison bar charts
├── schedulers/
│   ├── fcfs.py               # First Come First Served
│   ├── round_robin.py        # Round Robin (configurable quantum)
│   ├── priority.py           # Non-preemptive Priority Scheduling
│   └── custom.py             # Custom Hybrid Scheduler (region fairness + anti-starvation)
└── docs/
    └── ECE402C-ProjectProposal.pdf
```

---

## Scheduling Algorithms

| Scheduler | Description |
|---|---|
| **FCFS** | Requests are processed strictly in order of arrival. Simple but susceptible to convoy effect. |
| **Round Robin** | Each request gets a fixed time quantum (default: 5 units). Promotes fairness but increases overhead. |
| **Priority** | Higher-priority requests are serviced first. Efficient for VIP/time-critical requests but risks starvation. |
| **Custom (Hybrid)** | Combines region-based round-robin with priority scheduling and dynamic starvation promotion. Low-priority requests are boosted after waiting beyond a threshold. |

---

## Request Model

Each simulated ticket request has the following attributes:

| Field | Description |
|---|---|
| `id` | Unique request identifier |
| `arrival_time` | When the request enters the system |
| `burst_time` | Processing time required (1–20 units) |
| `priority` | 1 (highest) to 5 (lowest) |
| `region` | Geographic region: West, East, Central, South, North |

---

## Evaluation Metrics

- **Average Waiting Time** — average time a request sits in the queue before being serviced
- **Average Turnaround Time** — average time from submission to completion
- **Throughput** — number of requests completed per time unit
- **Starvation Rate** — fraction of requests that waited beyond the starvation threshold

---

## Getting Started

### Prerequisites

- Python 3.11+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/josephc8464/ECE402C_Project.git
cd ECE402C_Project

# Create and activate a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install matplotlib
```

### Running the Simulation

```bash
python main.py
```

This will:
1. Generate 1,000 synthetic ticket requests
2. Run all four schedulers
3. Print metrics to the terminal
4. Display a 4-panel comparison chart

### Adjusting Load

In `main.py`, change the `N` variable to simulate heavier traffic:

```python
N = 1000   # default
N = 5000   # medium load
N = 10000  # heavy load (as described in proposal)
```

### Adjusting Scheduler Parameters

```python
# Round Robin quantum (in main.py)
round_robin(requests, quantum=5)

# Custom scheduler — tune starvation threshold
custom_scheduler(requests, quantum=5, starvation_threshold=50)
```

---

## Expected Results

| Scheduler | Waiting Time | Fairness | Starvation Risk |
|---|---|---|---|
| FCFS | High (convoy effect) | Low | Low |
| Round Robin | Medium | High | Very Low |
| Priority | Low (for high-priority) | Low | High |
| Custom | Medium-Low | High | Very Low |

The custom scheduler is designed to find the best of both worlds — reducing starvation while preserving responsiveness for higher-priority requests.

---

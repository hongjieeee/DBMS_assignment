import csv
import os

def log_to_csv(
    technique,
    iterations,
    total_time,
    avg_latency,
    throughput,
    cpu_time
):
    file_exists = os.path.isfile("results.csv")

    with open("results.csv", "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "Technique",
                "Iterations",
                "Total_Time_s",
                "Avg_Latency_ms",
                "Throughput_qps",
                "CPU_Time_s"
            ])

        writer.writerow([
            technique,
            iterations,
            f"{total_time:.6f}",
            f"{avg_latency:.6f}",
            f"{throughput:.2f}",
            f"{cpu_time:.2f}"
        ])

Overview

This repository contains the source code, datasets, and benchmarking scripts used in the experimental evaluation of SQL Injection (SQLi) prevention techniques in a MySQL Database Management System (DBMS).

The objective of this project is to quantitatively measure the performance overhead introduced by common SQL Injection prevention techniques when compared to unsafe SQL execution. The evaluation focuses on query latency, CPU utilization, and throughput, highlighting the trade‑off between database security and system efficiency.

This work supports the experimental results presented in the accompanying IEEE‑style research paper.

SQL Injection Handling Techniques Evaluated

The following SQL injection handling techniques are benchmarked:

Unsafe SQL Queries (Baseline)

Direct string‑concatenated SQL queries

No SQL Injection protection

Prepared Statements

Parameterized queries using MySQL Connector/Python

Stored Procedures

Server‑side stored procedure invocation

Input Validation

Application‑level sanitization before query execution

Experimental Environment

Database: MySQL (Local instance)

Dataset Size: 99,991 records

Workload: Read‑only SELECT queries

Iterations per Technique: 10,000

Client: Python 3

Operating Mode: Single‑machine, localhost execution

Evaluation Metrics

The following metrics are collected for each technique:

Average Latency (ms)
Time taken to execute a single query.

CPU Utilization (%)
Average CPU usage during query execution.

Throughput (queries/second)
Number of queries processed per second.

Latency Overhead (%)
Computed relative to the Baseline:

(Latency_technique − Latency_baseline) / Latency_baseline × 100


CPU Overhead (%)
Computed relative to the Baseline:

CPU_technique − CPU_baseline

Repository Structure
.
├── baseline.py                 # Unsafe SQL query benchmark
├── prepared_statement.py       # Prepared statement benchmark
├── stored_procedures.py         # Stored procedure benchmark
├── input_validation.py         # Input validation benchmark
├── run_all_benchmarks.py       # Executes all benchmark scripts
├── log_csv.py                  # Shared CSV logging utility
├── config.py                   # Database configuration and constants
├── dataset/
│   └── SocialMediaUsersDataset.csv
└── README.md

Configuration
config.py

Edit this file before running experiments:

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "DBMS"
}

TEST_COUNTRY = "United States"
ITERATIONS = 10000

How to Run the Experiments
Step 1: Install Dependencies
pip install mysql-connector-python psutil numpy pandas

Step 2: Run All Benchmarks
python run_all_benchmarks.py


Each technique is executed sequentially, and results are logged to results.csv.

Output

The benchmarking scripts generate:

results.csv – Raw results per technique

combined_results.csv – Aggregated output (optional)

Example output format:

Technique	Iterations	Avg Latency (ms)	CPU Usage (%)	Throughput (qps)
Baseline	10000	23.81	2.59	42.00
Prepared Statement	10000	24.60	2.65	40.65
Reproducibility

To ensure reproducibility:

All scripts are deterministic

Dataset is included

Experimental parameters are centralized in config.py

Results are logged in CSV format

Limitations

Experiments are conducted on a local MySQL instance

No concurrent clients

No cold‑start or distributed database configuration

Results reflect single‑machine performance characteristics

These limitations are acknowledged in the paper’s discussion section.

License

This project is intended for academic and educational purposes only.

Citation

If you use this code or dataset, please cite the associated research paper or acknowledge the repository accordingly.

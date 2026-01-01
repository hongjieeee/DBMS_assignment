# SQL Injection Prevention Performance Benchmark

## Overview
This repository contains the source code, datasets, and benchmarking scripts used in the experimental evaluation of **SQL Injection (SQLi) prevention techniques** in a MySQL Database Management System (DBMS).

The objective of this project is to **quantitatively measure the performance overhead** introduced by common SQL Injection prevention techniques when compared to unsafe SQL execution. The evaluation focuses on **query latency**, **CPU utilization**, and **throughput**, highlighting the trade‑off between database security and system efficiency.

This work supports the experimental results presented in the accompanying IEEE-style research paper.

---

## SQL Injection Handling Techniques Evaluated
The following SQL injection handling techniques are benchmarked:

1. **Unsafe SQL Queries (Baseline)**  
   - Direct string-concatenated SQL queries  
   - No SQL Injection protection  

2. **Prepared Statements**  
   - Parameterized queries using MySQL Connector/Python  

3. **Stored Procedures**  
   - Server-side stored procedure invocation  

4. **Input Validation**  
   - Application-level sanitization before query execution  

---

## Experimental Environment
- **Database**: MySQL (Local instance)
- **Dataset Size**: 99,991 records
- **Workload**: Read-only SELECT queries
- **Iterations per Technique**: 10,000
- **Client**: Python 3
- **Operating Mode**: Single-machine, localhost execution

---

## Evaluation Metrics
The following metrics are collected for each technique:

- **Average Latency (ms)**  
  Time taken to execute a single query.

- **CPU Utilization (%)**  
  Average CPU usage during query execution.

- **Throughput (queries/second)**  
  Number of queries processed per second.

- **Latency Overhead (%)**  
  Computed relative to the Baseline:

- **CPU Overhead (%)**  
Computed relative to the Baseline:

---

## Configuration

### `config.py`
Edit this file before running experiments:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "DBMS"
}
TEST_COUNTRY = "United States"
ITERATIONS = 10000
```

## How to Run the Experiments
Step 1: Install Dependencies
   pip install mysql-connector-python psutil numpy pandas

Step 2: Run All Scirpts
   python run_script.py


Each technique is executed sequentially, and results are logged to results.csv.

##Reproducibility

To ensure reproducibility:

    All scripts are deterministic
    
    Dataset is included
    
    Experimental parameters are centralized in config.py
    
    Results are logged in CSV format

Limitations

    Experiments are conducted on a local MySQL instance

    No concurrent clients

    No cold-start or distributed database configuration

    Results reflect single-machine performance characteristics


License

    This project is intended for academic and educational purposes only.

Citation

    If you use this code or dataset, please cite the associated research paper or acknowledge the repository accordingly.

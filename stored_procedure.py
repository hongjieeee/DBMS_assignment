import mysql.connector
import time
import psutil
from config import DB_CONFIG, TEST_COUNTRY, ITERATIONS
from log_csv import log_to_csv

process = psutil.Process()

db = mysql.connector.connect(**DB_CONFIG)
cursor = db.cursor()

cursor.execute("FLUSH TABLES;")

latencies = []

cpu_start = process.cpu_times()
start = time.time()

for _ in range(ITERATIONS):
    t0 = time.time()
    cursor.callproc("getUsersByCountry", (TEST_COUNTRY,))
    for r in cursor.stored_results():
        r.fetchall()
    latencies.append((time.time() - t0) * 1000)

total_time = time.time() - start
cpu_end = process.cpu_times()

log_to_csv(
    "Stored Procedure",
    ITERATIONS,
    total_time,
    sum(latencies) / len(latencies),
    ITERATIONS / total_time,
    (cpu_end.user + cpu_end.system) - (cpu_start.user + cpu_start.system)
)

cursor.close()
db.close()

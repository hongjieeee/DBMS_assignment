import mysql.connector
import time
import psutil
import re
from config import DB_CONFIG, TEST_COUNTRY, ITERATIONS
from log_csv import log_to_csv

process = psutil.Process()
safe_country = re.sub(r"[^a-zA-Z\s]", "", TEST_COUNTRY)

db = mysql.connector.connect(**DB_CONFIG)
cursor = db.cursor()

cursor.execute("FLUSH TABLES;")

latencies = []

cpu_start = process.cpu_times()
start = time.time()

for _ in range(ITERATIONS):
    t0 = time.time()
    query = f"SELECT * FROM users WHERE Country = '{safe_country}'"
    cursor.execute(query)
    cursor.fetchall()
    latencies.append((time.time() - t0) * 1000)

total_time = time.time() - start
cpu_end = process.cpu_times()

log_to_csv(
    "Input Validation",
    ITERATIONS,
    total_time,
    sum(latencies) / len(latencies),
    ITERATIONS / total_time,
    (cpu_end.user + cpu_end.system) - (cpu_start.user + cpu_start.system)
)

cursor.close()
db.close()

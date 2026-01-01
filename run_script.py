import subprocess

scripts = [
    "baseline.py",
    "prepared_statement.py",
    "stored_procedure.py",
    "input_validation.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python3", script], check=True)

print("\nAll benchmarks completed. Results saved to results.csv")

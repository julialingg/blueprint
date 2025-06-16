import csv
import subprocess
import re

csv_file_path = "dataset.csv"

def extract_pr_number(pr_url):
    match = re.search(r'/pull/(\d+)', pr_url)
    return match.group(1) if match else None

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pr_url = row['PR'].strip()
        base_commit = row['base_commit'].strip()
        pr_number = extract_pr_number(pr_url)

        if not pr_number or not base_commit:
            print(f"Skipping row: PR={pr_url}, base_commit={base_commit}")
            continue

        branch_name = f"{pr_number}"
        print(f"\nCreating branch '{branch_name}' from base commit {base_commit}...")

        try:
            subprocess.run(["git", "checkout", base_commit], check=True)
            subprocess.run(["git", "checkout", "-b", branch_name], check=True)
            subprocess.run(["git", "push", "-u", "origin", branch_name], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error while processing PR #{pr_number}: {e}")

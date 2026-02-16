#!/usr/bin/python3
"""
1-export_to_CSV.py
Exports all tasks for a given employee ID to CSV in the exact format:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name: USER_ID.csv
"""
import sys
import csv
import requests


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID", file=sys.stderr)
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer", file=sys.stderr)
        sys.exit(1)

    base = "https://jsonplaceholder.typicode.com"

    user_resp = requests.get(f"{base}/users/{employee_id}")
    if user_resp.status_code != 200:
        sys.exit(1)
    user = user_resp.json()
    username = user.get("username")

    todos_resp = requests.get(f"{base}/todos", params={"userId": employee_id})
    if todos_resp.status_code != 200:
        sys.exit(1)
    todos = todos_resp.json()

    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([employee_id, username, t.get("completed"), t.get("title")])


if __name__ == "__main__":
    main()

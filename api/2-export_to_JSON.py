#!/usr/bin/python3
"""
2-export_to_JSON.py
Exports tasks for a given employee ID to JSON in the exact format:
{ "USER_ID": [
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
    ...
]}
File name: USER_ID.json
"""
import sys
import json
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

    result = {
        str(employee_id): [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username,
            }
            for t in todos
        ]
    }

    filename = f"{employee_id}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f)


if __name__ == "__main__":
    main()

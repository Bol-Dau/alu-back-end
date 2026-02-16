#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
Fetches and displays TODO list progress for a given employee ID
from JSONPlaceholder (https://jsonplaceholder.typicode.com).
Requirements:
- Uses requests
- Takes an integer employee ID as argument
- Prints in the exact specified format
"""
import sys
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

    # Fetch user info
    user_resp = requests.get(f"{base}/users/{employee_id}")
    if user_resp.status_code != 200:
        sys.exit(1)
    user = user_resp.json()
    employee_name = user.get("name")

    # Fetch todos for the employee
    todos_resp = requests.get(f"{base}/todos", params={"userId": employee_id})
    if todos_resp.status_code != 200:
        sys.exit(1)
    todos = todos_resp.json()

    completed = [t for t in todos if t.get("completed") is True]

    print(f"Employee {employee_name} is done with tasks({len(completed)}/{len(todos)}):")
    for task in completed:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()

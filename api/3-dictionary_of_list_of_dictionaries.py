#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py
Exports all tasks from all employees to JSON in the exact format:
{
  "USER_ID": [
    {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
    ...
  ],
  "USER_ID": [...]
}
File name: todo_all_employees.json
"""
import json
import requests


def main():
    base = "https://jsonplaceholder.typicode.com"

    # Fetch all users and all todos once, then assemble
    users_resp = requests.get(f"{base}/users")
    todos_resp = requests.get(f"{base}/todos")
    if users_resp.status_code != 200 or todos_resp.status_code != 200:
        raise SystemExit(1)

    users = users_resp.json()
    todos = todos_resp.json()

    # Map userId -> username
    user_map = {u.get("id"): u.get("username") for u in users}

    result = {}
    # Initialize keys to ensure all users appear even if they had zero todos (for completeness)
    for uid in user_map:
        result[str(uid)] = []

    for t in todos:
        uid = t.get("userId")
        result[str(uid)].append(
            {
                "username": user_map.get(uid),
                "task": t.get("title"),
                "completed": t.get("completed"),
            }
        )

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(result, f)


if __name__ == "__main__":
    main()

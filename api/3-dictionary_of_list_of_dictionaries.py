#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py

Exports all tasks from all employees to JSON in the exact format:
{
  "USER_ID": [
    {"username": "USERNAME", "task": "TASK_TITLE",
     "completed": TASK_COMPLETED_STATUS},
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

    users_resp = requests.get(f"{base}/users")
    todos_resp = requests.get(f"{base}/todos")
    if users_resp.status_code != 200 or todos_resp.status_code != 200:
        raise SystemExit(1)

    users = users_resp.json()
    todos = todos_resp.json()

    user_map = {user.get("id"): user.get("username") for user in users}

    result = {}
    for uid in user_map:
        result[str(uid)] = []

    for todo in todos:
        uid = todo.get("userId")
        result[str(uid)].append(
            {
                "username": user_map.get(uid),
                "task": todo.get("title"),
                "completed": todo.get("completed"),
            }
        )

    with open("todo_all_employees.json", "w", encoding="utf-8") as fobj:
        json.dump(result, fobj)


if __name__ == "__main__":
    main()

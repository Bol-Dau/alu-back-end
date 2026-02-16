#!/usr/bin/python3
"""
Exports all employees' TODO list data to a JSON file.
File: todo_all_employees.json
"""

import json
import requests


def fetch_all_employees():
    """Fetch all employees from the API."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()


def fetch_employee_todos(employee_id):
    """Fetch all TODO tasks for a given employee."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": employee_id})
    if response.status_code != 200:
        return []
    return response.json()


def export_all_to_json():
    """Fetch all employees and their tasks, export to JSON file."""
    all_employees = fetch_all_employees()
    data = {}

    for employee in all_employees:
        user_id = str(employee.get("id"))
        username = employee.get("username")
        todos = fetch_employee_todos(employee.get("id"))

        data[user_id] = []
        for task in todos:
            data[user_id].append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)


def main():
    """Main program entry point."""
    export_all_to_json()


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
Exports employee TODO list data to a JSON file.
Usage: ./2-export_to_JSON.py EMPLOYEE_ID
"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee information from the API."""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    if response.status_code != 200:
        return {}
    return response.json()


def fetch_employee_todos(employee_id):
    """Fetch all TODO tasks for a given employee."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": employee_id})
    if response.status_code != 200:
        return []
    return response.json()


def export_to_json(employee_id, username, todos):
    """Export tasks to a JSON file in the required format."""
    filename = "{}.json".format(employee_id)
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): tasks}

    with open(filename, "w") as json_file:
        json.dump(data, json_file)


def main():
    """Main program entry point."""
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py EMPLOYEE_ID")
        sys.exit(0)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer")
        sys.exit(0)

    employee = fetch_employee_data(employee_id)
    if not employee:
        print("Employee not found.")
        sys.exit(0)

    todos = fetch_employee_todos(employee_id)
    username = employee.get("username")

    export_to_json(employee_id, username, todos)


if __name__ == "__main__":
    main()

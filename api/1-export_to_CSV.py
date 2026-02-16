#!/usr/bin/python3
"""
Exports employee TODO list progress to a CSV file
"""
import requests
import csv
import sys


def fetch_employee_data(employee_id):
    """Fetch employee data from the REST API."""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    return response.json()


def fetch_employee_todos(employee_id):
    """Fetch TODO list for the given employee."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": employee_id})
    return response.json()


def export_to_csv(employee_id, username, todos):
    """Export employee TODOs to a CSV file."""
    filename = "{}.csv".format(employee_id)
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


def main():
    """Main function."""
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer")
        sys.exit(1)

    employee = fetch_employee_data(employee_id)
    todos = fetch_employee_todos(employee_id)
    username = employee.get("username")

    export_to_csv(employee_id, username, todos)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
Module for fetching employee TODO list progress from REST API
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays employee TODO list progress
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = 0
    completed_titles = []
    for task in todos_data:
        if task.get("completed"):
            completed_tasks += 1
            completed_titles.append(task.get('title'))
    print(f"Employee {employee_name} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")
    for title in completed_titles:
        print(f"\t {title}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

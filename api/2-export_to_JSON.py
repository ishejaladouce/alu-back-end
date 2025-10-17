#!/usr/bin/python3
"""
Module for exporting employee TODO list to JSON format
"""

import json
import requests
import sys


def export_to_json(employee_id):
    """
    Exports employee TODO list to JSON file
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    user_id = user_data.get("id")
    username = user_data.get("username")
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()
    tasks_list = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)
    json_data = {str(user_id): tasks_list}
    filename = f"{user_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)
    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

#!/usr/bin/python3
"""
Module for exporting all employees TODO lists to JSON format
"""

import json
import requests


def export_all_to_json():
    """
    Exports all employees TODO lists to JSON file
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users_response = requests.get(f"{base_url}/users")
    users_data = users_response.json()
    all_employees_data = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        todos_response = requests.get(f"{base_url}/users/{user_id}/todos")
        todos_data = todos_response.json()
        user_tasks = []
        for task in todos_data:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            user_tasks.append(task_dict)
        all_employees_data[str(user_id)] = user_tasks
    filename = "todo_all_employees.json"
    with open(filename, 'w') as jsonfile:
        json.dump(all_employees_data, jsonfile)


if __name__ == "__main__":
    export_all_to_json()

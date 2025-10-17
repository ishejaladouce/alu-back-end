#!/usr/bin/python3
"""
Module for exporting employee TODO list to CSV format
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Exports employee TODO list to CSV file
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    user_id = user_data.get("id")
    username = user_data.get("username")
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            task_completed = task.get("completed")
            task_title = task.get("title")
            csv_writer.writerow([user_id, username,
                                task_completed, task_title])
    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

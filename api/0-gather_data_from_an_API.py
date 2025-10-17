#!/usr/bin/python3
"""
Module for fetching employee TODO list progress from REST API
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays employee TODO list progress
    
    Args:
        employee_id (int): The employee ID to fetch data for
        
    Raises:
        ValueError: If employee_id is not a positive integer
        SystemExit: If API request fails or employee not found
    """
    try:
        # Validate employee_id
        if not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer")
        
        # Base URL for the JSONPlaceholder API
        base_url = "https://jsonplaceholder.typicode.com"
        
        # Fetch employee details
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        if user_response.status_code != 200:
            print(f"Error: Employee with ID {employee_id} not found")
            sys.exit(1)
            
        user_data = user_response.json()
        employee_name = user_data.get("name")
        
        # Fetch employee TODO list
        todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
        if todos_response.status_code != 200:
            print(f"Error: Could not fetch TODO list for employee {employee_id}")
            sys.exit(1)
            
        todos_data = todos_response.json()
        
        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for task in todos_data if task.get("completed"))
        
        # Display progress
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        
        # Display completed tasks
        for task in todos_data:
            if task.get("completed"):
                print(f"\t {task.get('title')}")
                
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to API - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


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

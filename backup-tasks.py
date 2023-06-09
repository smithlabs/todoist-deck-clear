"""Todoist Task Backup

This script creates backups of your Todoist tasks by retrieving your
current tasks from your specified Todoist projects from the Todoist API
and saves them as serialized JSON files. The backup files are stored
in the 'backup/' folder created in the script's directory.

Specify the projects you want to backup in the 'settings.json' file.

Each project's backup file is named to match its corresponding Todoist
Project name (e.g., A project called Work saves as 'backup/work.json').

It's required to generate a Todoist API token and place it in a
'token' file in the same folder as the script.

The following modules are used:
    * argparse - adds runtime flags
    * json - for serializing the tasks from the API
    * todoist_api_python - for making API calls to Todoist
"""

import argparse

import json

from todoist_api_python.api import TodoistAPI

def object_to_dict(obj):
    if isinstance(obj, (int, float, str, bool, type(None))):
        # Base case: handle basic types
        return obj
    elif isinstance(obj, dict):
        # Recursively convert dictionary values
        return {key: object_to_dict(value) for key, value in obj.items()}
    elif isinstance(obj, (list, tuple)):
        # Recursively convert list/tuple elements
        return [object_to_dict(item) for item in obj]
    else:
        # Convert custom object attributes to a dictionary
        return object_to_dict(obj.__dict__)

def backup_tasks(api, project_name, dry_run=False):
    """Retrieves tasks from Todoist API and serializes/saves as JSON

    Parameters
    ----------
    api : str
        Your API token from Todoist
    project_name : 

    """
    projects = api.get_projects()
    project_dicts = [project.__dict__ for project in projects]

    target_project_id = None

    for project_dict in project_dicts:
        if project_dict['name'] == project_name:
            target_project_id = project_dict['id']
            break

    if target_project_id:
        tasks = api.get_tasks(project_id=target_project_id)
        task_dicts = [object_to_dict(task) for task in tasks]
        
        if dry_run:
            print(f"Dry run: Backup for project '{project_name}' would be created.")
            print("Dry run: Tasks to be backed up:")
            for task_dict in task_dicts:
                print(f"- Task: {task_dict['content']} (Project: {project_name})")
        else:
            json_array = json.dumps(task_dicts, indent=2)  # Format the JSON array with indentation and line spacing
            filename = f"backup/{project_name.lower()}.json"
            with open(filename, "w") as file:
                file.write(json_array)
                print(f"Backup for project '{project_name}' has been created: {filename}")
            
            for task_dict in task_dicts:
                print(f"- Task: {task_dict['content']} (Project: {project_name})")

def main():
    parser = argparse.ArgumentParser(description="Backup tasks from Todoist projects.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without creating backups")
    args = parser.parse_args()

    with open("token", "r") as file:
        api_key = file.read().strip()

    api = TodoistAPI(api_key)

    with open("settings.json", "r") as settings_file:
        settings = json.load(settings_file)
    
    project_names = settings.get("projects", [])
    if not project_names:
        print("No project names found in the settings file.")
        return

    for project_name in project_names:
        backup_tasks(api, project_name, dry_run=args.dry_run)


if __name__ == "__main__":
    main()

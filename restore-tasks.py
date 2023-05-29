import argparse
import json
from todoist_api_python.api import TodoistAPI

# Reading the API key from the file
with open("token", "r") as file:
    api_key = file.read().strip()

# Create an instance of the TodoistAPI using the API key
api = TodoistAPI(api_key)

def restore_backups(target_project_name, dry_run=False):
    target_project_id = None

    projects = api.get_projects()
    project_dicts = [vars(project) for project in projects]

    for project_dict in project_dicts:
        if project_dict['name'] == target_project_name:
            target_project_id = project_dict['id']
            break

    if not target_project_id:
        print(f"Project '{target_project_name}' does not exist.")
        return

    try:
        # Read the tasks from the backup JSON file
        with open(f"backup/{target_project_name.lower()}.json", "r") as file:
            tasks = json.load(file)

        task_ids = {}  # Dictionary to store the mapping of original IDs to current IDs

        for task in tasks:
            if task["parent_id"] is None:
                # Top-level task, create it directly
                if dry_run:
                    print(f"Creating task called '{task['content']}' under project named '{target_project_name}'")
                else:
                    created_task = api.add_task(project_id=target_project_id, content=task["content"])
                    task_ids[task["id"]] = vars(created_task)["id"]
                    print(f"Created task called '{task['content']}' under project named '{target_project_name}'")
            else:
                # Subtask, find the parent task ID and create the subtask
                parent_id = task_ids.get(task["parent_id"])
                if parent_id is not None:
                    if dry_run:
                        parent_task_name = next((t["content"] for t in tasks if t["id"] == task["parent_id"]), None)
                        print(f"Creating sub-task called '{task['content']}' under parent task name '{parent_task_name}'")
                    else:
                        created_task = api.add_task(project_id=target_project_id, content=task["content"], parent_id=parent_id)
                        task_ids[task["id"]] = vars(created_task)["id"]
                        parent_task_name = next((t["content"] for t in tasks if t["id"] == task["parent_id"]), None)
                        print(f"Created sub-task called '{task['content']}' under parent task name '{parent_task_name}'")
    except Exception as error:
        print(error)

def main():
    parser = argparse.ArgumentParser(description="Restore backups of tasks to Todoist.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without making any changes")
    args = parser.parse_args()

    with open("settings.json", "r") as settings_file:
        settings = json.load(settings_file)

    project_names = settings.get("projects", [])
    if not project_names:
        print("No project names found in the settings file.")
        return

    for project_name in project_names:
        print(f"Restoring backups for project '{project_name}'...")
        restore_backups(project_name, dry_run=args.dry_run)

    print("All backups have been restored.")

if __name__ == "__main__":
    main()

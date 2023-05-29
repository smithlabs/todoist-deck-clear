import argparse
import json
from todoist_api_python.api import TodoistAPI

def delete_tasks(api_key, project_names, dry_run=False):
    api = TodoistAPI(api_key)

    try:
        projects = api.get_projects()
        project_dicts = [project.__dict__ for project in projects]

        for project_dict in project_dicts:
            if project_dict['name'] in project_names:
                target_project_id = project_dict['id']
                tasks = api.get_tasks(project_id=target_project_id)
                task_dicts = [task.__dict__ for task in tasks]

                for task_dict in task_dicts:
                    if dry_run:
                        print(f"Dry run: Deleting task: '{task_dict['content']}' in project '{project_dict['name']}'")
                    else:
                        api.delete_task(task_id=task_dict['id'])
                        print(f"Deleting task: '{task_dict['content']}' in project '{project_dict['name']}'")
            else:
                print(f"Project '{project_dict['name']}' not found in the settings.")

    except Exception as error:
        print(error)

def main():
    parser = argparse.ArgumentParser(description="Delete tasks from Todoist projects.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without actually deleting tasks")
    args = parser.parse_args()

    with open("token", "r") as file:
        api_key = file.read().strip()

    with open("settings.json", "r") as settings_file:
        settings = json.load(settings_file)

    project_names = settings.get("projects", [])
    if not project_names:
        print("No project names found in the settings file.")
        return

    delete_tasks(api_key, project_names, dry_run=args.dry_run)

if __name__ == "__main__":
    main()

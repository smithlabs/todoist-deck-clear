### Getting Started

To get started with the Todoist Task Management Scripts, follow the steps below:

1. Clone the repository:
   ```
   git clone https://github.com/smithlabs/todoist-task-scripts.git
   ```

2. Create the `settings.json` file:
   - Navigate to the project directory.
   - Create a file named `settings.json`.
   - Inside `settings.json`, specify the project names you want to perform actions on. For example:
     ```json
     {
         "projects": ["Project 1", "Project 2"]
     }
     ```

3. Backup Tasks:
   - The `backup_tasks.py` script allows you to create backups of tasks from Todoist projects.
   - Ensure you have the required dependencies installed by running `pip install -r requirements.txt`.
   - Obtain a Todoist API token and place it in a file named `token` in the project directory.
   - Modify the `settings.json` file to include the project names you want to back up.
   - Run the script using the command `python backup_tasks.py`.

4. Delete Tasks:
   - The `delete_tasks.py` script enables you to delete tasks from Todoist projects.
   - Ensure you have the required dependencies installed by running `pip install -r requirements.txt`.
   - Obtain a Todoist API token and place it in a file named `token` in the project directory.
   - Modify the `settings.json` file to include the project names from which you want to delete tasks.
   - Run the script using the command `python delete_tasks.py`.

5. Restore Tasks:
   - The `restore_tasks.py` script allows you to restore backups of tasks to Todoist projects.
   - Ensure you have the required dependencies installed by running `pip install -r requirements.txt`.
   - Obtain a Todoist API token and place it in a file named `token` in the project directory.
   - Ensure that backup JSON files are located in the "backup" folder within the project directory, following the lowercase naming convention.
   - Modify the `settings.json` file to include the project names you want to restore tasks to.
   - Run the script using the command `python restore_tasks.py`.

Make sure to review the script files and configure the settings appropriately before running any scripts. These scripts provide convenient automation for managing tasks in Todoist, helping you maintain productivity and organization.

### How Tasks Are Backed Up in JSON

The backup script creates a dedicated folder named "backup" in the project directory. Within this folder, it generates one JSON file per project specified in the `settings.json` file. Each JSON file contains the serialized representation of tasks and sub-tasks, allowing for easy recreation using the restore script.

Here is an example directory structure:

```
backup
├── project1.json
├── project2 ideas.json
├── project3.json
└── inbox.json
```

For instance, let's consider the contents of the `backup/project1.json` file, which includes two tasks: "Buy eggs" and "Buy milk".

```json
[
  {
    "assignee_id": null,
    "assigner_id": null,
    "comment_count": 0,
    "is_completed": false,
    "content": "Buy eggs",
    "created_at": "2023-05-28T21:02:06.488170Z",
    "creator_id": "42970196",
    "description": "",
    "due": null,
    "id": "6917477720",
    "labels": [],
    "order": 1,
    "parent_id": null,
    "priority": 1,
    "project_id": "123456789",
    "section_id": null,
    "url": "https://todoist.com/showTask?id=123456789",
    "sync_id": null
  },
  {
    "assignee_id": null,
    "assigner_id": null,
    "comment_count": 0,
    "is_completed": false,
    "content": "Buy milk",
    "created_at": "2023-05-28T21:02:06.891954Z",
    "creator_id": "42970196",
    "description": "",
    "due": null,
    "id": "987654321",
    "labels": [],
    "order": 2,
    "parent_id": null,
    "priority": 1,
    "project_id": "2312208059",
    "section_id": null,
    "url": "https://todoist.com/showTask?id=987654321",
    "sync_id": null
  }
]
```

The JSON file includes detailed information about each task, such as its content, creation date, project ID, URL, and more. This serialized format allows for seamless restoration of tasks and their associated properties using the restore script.

### Backup Tasks Script

The "Backup Tasks" script is a Python script that allows you to back up tasks from Todoist projects. It uses the Todoist API to retrieve project information and tasks, and then creates backups in JSON format.

#### Details

To use the script, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Obtain a Todoist API token. You can create one by following the instructions [here](https://developer.todoist.com/guides/#step-1-create-a-new-app).
4. Create a file named `token` in the project directory and paste your API token into it.
5. Create a file named `settings.json` in the project directory. This file should contain a list of project names you want to back up. For example:
    ```json
    {
        "projects": ["Project 1", "Project 2"]
    }
    ```
6. Run the script using the command `python backup_tasks.py`. By default, the script will create backups without a dry run. If you want to perform a dry run without actually creating backups, use the `--dry-run` flag.
7. The script will create backup files for each project in a folder named "backup" within the project directory. The backup files will be named in lowercase using the project names. For example, for a project named "Project 1", the backup file will be "backup/project 1.json".

#### Example Output

During the execution of the script, you will see output indicating the progress and status of the backup process. Here's an example of the output:

```
Backup for project 'Project 1' has been created: backup/project 1.json
Tasks backed up:
- Task: Task 1 (Project: Project 1)
- Task: Task 2 (Project: Project 1)
...
Backup for project 'Project 2' has been created: backup/project 2.json
Tasks backed up:
- Task: Task 1 (Project: Project 2)
- Task: Task 2 (Project: Project 2)
...
All backups have been created.
```

#### Additional Notes

- The script uses the `argparse` module to parse command-line arguments. You can run `python backup_tasks.py --help` to see the available options.
- The `object_to_dict` function is a helper function used to convert objects to dictionaries. It recursively handles different types of objects and their attributes.
- The script assumes the presence of the `todoist_api_python` package, which can be installed via `pip`. Make sure you have it installed or include it in your `requirements.txt` file.
- The script reads the Todoist API token from a file named `token` in the project directory. Make sure to replace the content of this file with your own API token.

Feel free to modify and adapt the script according to your needs. Happy task backup!


### Delete Tasks Script

#### Example Output

During the execution of the script, you will see output indicating the progress and status of the task deletion process. Here's an example of the output:

```
Deleting task: 'Task 1' in project 'Project 1'
Deleting task: 'Task 2' in project 'Project 1'
...
Deleting task: 'Task 1' in project 'Project 2'
Deleting task: 'Task 2' in project 'Project 2'
...
```

#### Additional Notes

- The script uses the `argparse` module to parse command-line arguments. You can run `python delete_tasks.py --help` to see the available options.
- The script assumes the presence of the `todoist_api_python` package, which can be installed via `pip`. Make sure you have it installed or include it in your `requirements.txt` file.
- The script reads the Todoist API token from a file named `token` in the project directory. Make sure to replace the content of this file with your own API token.
- The script reads the project names to delete tasks from the `settings.json` file. Make sure to update the list of project names accordingly.

Feel free to modify and adapt the script according to your needs. Use it responsibly to manage your Todoist tasks efficiently!

### Restore Tasks

The "Restore Tasks" script is a Python script that allows you to restore backups of tasks to Todoist projects. It utilizes the Todoist API to create tasks based on the information provided in backup JSON files.

#### Usage

1. Create backup JSON files for the projects you want to restore tasks to. The backup files should be located in the "backup" folder within the project directory. The backup file names should be in lowercase and match the project names. For example, if you want to restore tasks for a project named "Project 1", the backup file should be named "backup/project 1.json".
2. Create a file named `settings.json` in the project directory. This file should contain a list of project names you want to restore tasks to. For example:
    ```json
    {
        "projects": ["Project 1", "Project 2"]
    }
    ```
7. Run the script using the command `python restore_tasks.py`. By default, the script will restore tasks without performing a dry run. If you want to perform a dry run without actually making any changes, use the `--dry-run` flag.
8. The script will iterate through the specified projects, read the corresponding backup JSON files, and create tasks based on the backup data.

#### Example Output

During the execution of the script, you will see output indicating the progress and status of the task restoration process. Here's an example of the output:

```
Restoring backups for project 'Project 1'...
Created task called 'Task 1' under project named 'Project 1'
Created task called 'Task 2' under project named 'Project 1'
...

Restoring backups for project 'Project 2'...
Created task called 'Task 1' under project named 'Project 2'
Created task called 'Task 2' under project named 'Project 2'
...
```

#### Additional Notes

- The script assumes the presence of the `todoist_api_python` package, which can be installed via `pip`. Make sure you have it installed or include it in your `requirements.txt` file.
- The script reads the Todoist API token from a file named `token` in the project directory. Make sure to replace the content of this file with your own API token.
- The script reads the project names to restore tasks to from the `settings.json` file. Make sure to update the list of project names accordingly.
- The script locates the backup JSON files in the "backup" folder within the project directory. Make sure to place the backup files in the correct location and follow the lowercase naming convention.

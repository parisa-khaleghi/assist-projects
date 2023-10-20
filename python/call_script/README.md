# Git Commit Caller

This script allows you to call a specific function from an external Git repository in your Python project. It can be especially useful for automating the process of committing changes to your Git repositories with predefined messages and timestamps. 

## Usage

1. Clone the external Git repository to your local system, which contains the function you want to call.

2. Append the path to the external repository to your Python environment using the `sys.path.append` method. Make sure to replace the path in the code with the path to your cloned repository.

3. Import the specific function you want to call from the external script using `from git_commit import commit`, replacing `'git_commit'` with the name of the module in the external repository and `'commit'` with the name of the function.

4. Call the `commit` function with the required arguments. Here's a breakdown of the arguments:

   - `project_path`: The path to your Python project where you want to call the function.
   - `file_path`: The path to the specific file where you want to call the function.
   - `message`: The commit message you want to associate with this change.
   - `year`, `month`, `day`, `hour`, and `minute`: The timestamp for the commit.

## Example

In the provided code example, we call the `commit` function from the 'git_commit' module located in an external Git repository. We specify the paths to the project and file, the commit message, and the timestamp.

```python
print(commit('/Users/parisakhaleghi/Desktop/Coding/assist_projects',
             '/Users/parisakhaleghi/Desktop/Coding/assist_projects/python/call_script/call_script.py',
             'update: call the function from module',
             datetime.datetime.now().year,
             datetime.datetime.now().month-1,
             datetime.datetime.now().day,
             datetime.datetime.now().hour,
             datetime.datetime.now().minute
             ))

Feel free to adapt and use this script for your Git-related automation needs within your Python projects.

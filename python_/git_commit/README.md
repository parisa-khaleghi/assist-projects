# Custom Git Commit with Timezone Adjustment

This Python script allows you to make a custom Git commit with a specified date and time, along with a custom timezone adjustment. It can be useful in situations where you need precise control over the commit timestamp, such as when working on historical data or adjusting timestamps for different timezones.

## Prerequisites

Before using this script, ensure you have the following prerequisites:

- Python installed on your system.
- The GitPython library, which you can install using `pip`:


## Usage

To use this script to create a custom Git commit, follow these steps:

1. Clone or download this repository to your local machine.

2. Open the script `git-commit.py` and customize the following variables to match your project and desired commit details:
 - `project_path`: The path to your Git project's directory.
 - `file_path`: The path to the file you want to commit.
 - `message`: The commit message.
 - `year`, `month`, `day`, `hour`, and `minute`: The custom date and time for your commit.

3. Run the script using Python:


The script will add and commit the specified file with the provided details, including the custom timezone adjustment.

## Example

In the provided example, the script is configured to make a Git commit with the message "update: change timezone to Turkey" using the current date and time but adjusting the timezone to Turkey Standard Time (TRT).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to modify and adapt this script to suit your specific needs or use it as a reference for working with Git commits and timezones.


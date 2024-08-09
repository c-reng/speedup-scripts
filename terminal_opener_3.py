#Open up 3 tabs, cd to a directory, and run a script

import subprocess

# Common base path for all directories
base_path = "/path/to/your/base_directory"

# Define the directories, tab names, and commands for each tab
tabs = [
    (f"{base_path}/subdir1", "Tab 1", "echo 'Running script 1'; ./script1.csh"),
    (f"{base_path}/subdir2", "Tab 2", "echo 'Running script 2'; ./script2.csh"),
    (f"{base_path}/subdir3", "Tab 3", "echo 'Running script 3'; ./script3.csh")
]

# Build the command to open a single terminal with multiple tabs
cmd = ["gnome-terminal"]

for directory, tab_name, command in tabs:
    cmd.extend([
        "--tab", "--title", tab_name, "--", "tcsh", "-c", f"cd {directory}; {command}; exec tcsh"
    ])

# Execute the command
subprocess.Popen(cmd)

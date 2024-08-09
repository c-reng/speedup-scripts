#Open up 9 tabs, cd to a directory, and run a script

import subprocess

# Common base path for all directories
base_path = "/path/to/your/base_directory"

# Define the directories, tab names, and commands for each window and tab
tabs = [
    [
        (f"{base_path}/window1_subdir1", "Tab 1", "echo 'Running script 1'; ./script1.csh"),
        (f"{base_path}/window1_subdir2", "Tab 2", "echo 'Running script 2'; ./script2.csh"),
        (f"{base_path}/window1_subdir3", "Tab 3", "echo 'Running script 3'; ./script3.csh")
    ],
    [
        (f"{base_path}/window2_subdir1", "Tab 1", "echo 'Running script 4'; ./script4.csh"),
        (f"{base_path}/window2_subdir2", "Tab 2", "echo 'Running script 5'; ./script5.csh"),
        (f"{base_path}/window2_subdir3", "Tab 3", "echo 'Running script 6'; ./script6.csh")
    ],
    [
        (f"{base_path}/window3_subdir1", "Tab 1", "echo 'Running script 7'; ./script7.csh"),
        (f"{base_path}/window3_subdir2", "Tab 2", "echo 'Running script 8'; ./script8.csh"),
        (f"{base_path}/window3_subdir3", "Tab 3", "echo 'Running script 9'; ./script9.csh")
    ]
]

# Build the command to open multiple GNOME Terminal windows with multiple tabs
for i, window_tabs in enumerate(tabs):
    cmd = ["gnome-terminal"]
    for directory, tab_name, command in window_tabs:
        cmd.extend([
            "--tab", "--title", f"Window {i+1} - {tab_name}", "--", "tcsh", "-c", f"cd {directory}; {command}; exec tcsh"
        ])
    subprocess.Popen(cmd)

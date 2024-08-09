#Run back to back commands on new console window
import subprocess

# List of commands to run
commands = [
    "echo 'Running command 1'; ls -l",
    "echo 'Running command 2'; pwd",
    "echo 'Running command 3'; df -h",
    "echo 'Running command 4'; free -m",
    "echo 'Running command 5'; top -n 1"
]

# Combine commands into a single string with `;` to separate commands
combined_commands = " ; ".join(commands)

# Build the command to open a new Konsole window and execute the commands
cmd = ["konsole", "--hold", "-e", f"bash -c '{combined_commands}'"]

# Execute the command
subprocess.Popen(cmd)

import subprocess
import paramiko
import datetime
import os

# Base class for command execution
class CommandExecutor:
    def execute(self, command):
        raise NotImplementedError("Subclasses must implement execute() method")

# Concrete class for executing commands via SSH
class SSHCommandExecutor(CommandExecutor):
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password

    def execute(self, command):
        # Implement SSH command execution logic using paramiko or any SSH library
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.hostname, username=self.username, password=self.password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode("utf-8").strip()
        ssh.close()

        return output

# Factory Method pattern to create CommandExecutor instances dynamically
class CommandExecutorFactory:
    def create_executor(self):
        # Read hostname, username, and password from the "pass.txt" file
        desktop_path = os.path.expanduser("~/Desktop")
        logs_folder = os.path.join(desktop_path, "logs")
        pass_file = os.path.join(logs_folder, "pass.txt")

        if not os.path.exists(pass_file):
            raise FileNotFoundError("pass.txt file not found. Creating files for user to edit.")

        with open(pass_file, 'r') as file:
            hostname = file.readline().strip()
            username = file.readline().strip()
            password = file.readline().strip()

        return SSHCommandExecutor(hostname, username, password)

# Function to save command and its output to a text file without overwriting existing content
def save_to_file(command, output, filename):
    desktop_path = os.path.expanduser("~/Desktop")
    logs_folder = os.path.join(desktop_path, "logs")
    file_path = os.path.join(logs_folder, filename)

    with open(file_path, 'a') as file:
        file.write(f"Command: {command}\n")
        file.write(f"Output: {output}\n")
        file.write(f"Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

# Create pass.txt file for user to edit
def create_pass_file():
    desktop_path = os.path.expanduser("~/Desktop")
    logs_folder = os.path.join(desktop_path, "logs")
    pass_file = os.path.join(logs_folder, "pass.txt")

    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    with open(pass_file, 'w') as file:
        file.write("hostname\n")
        file.write("username\n")
        file.write("password\n")

    print("pass.txt file created in the logs folder on the desktop. Please edit the file with the correct information.")

# CLI interface for choosing the command to run
if __name__ == "__main__":
    try:
        factory = CommandExecutorFactory()
        ssh_executor = factory.create_executor()
    except FileNotFoundError as e:
        print(e)
        create_pass_file()
    else:
        while True:
            print("Choose a command to run:")
            print("1. Start Server")
            print("2. Generate Report")
            print("3. Shutdown")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                output = ssh_executor.execute("Desktop\START.bat")
                save_to_file("Desktop\START.bat", output, "command_results.txt")
                print("Example 1 Output:", output)
            elif choice == "2":
                output = ssh_executor.execute("python Desktop\Report.py")
                save_to_file("python Desktop\Report.py", output, "command_results.txt")
                print("Example 2 Output:", output)
            elif choice == "3":
                output = ssh_executor.execute("python Desktop\Shutdown.py")
                save_to_file("python Desktop\Shutdown.py", output, "command_results.txt")
                print("Example 3 Output:", output)
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

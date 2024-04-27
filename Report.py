import os
import psutil
from datetime import datetime
from operator import itemgetter

def list_running_programs():
    """
    Prints a list of all the programs that are currently running on the computer,
    along with their CPU and memory usage, and writes the results to a file in the
    "logs" folder on the desktop.
    The processes are sorted from highest to lowest memory usage.
    """
    # Get the path to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Create the "logs" folder if it doesn't exist
    logs_folder = os.path.join(desktop_path, "logs")
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)
    
    # Generate the file name
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"report_{current_datetime}.txt"
    file_path = os.path.join(logs_folder, file_name)
    
    with open(file_path, 'w') as file:
        # Get a list of all running processes
        processes = psutil.process_iter(['name', 'exe', 'cpu_percent', 'memory_percent'])
        
        # Sort the processes from highest to lowest memory usage
        sorted_processes = sorted(processes, key=lambda x: x.info['memory_percent'], reverse=True)
        
        # Write the name, executable path, CPU usage, and memory usage of each process to the file
        for process in sorted_processes:
            try:
                name = process.info['name']
                exe = process.info['exe']
                cpu_percent = process.info['cpu_percent']
                memory_percent = process.info['memory_percent']
                if exe:
                    file.write(f"{name} - {exe} - CPU: {cpu_percent:.2f}% - Memory: {memory_percent:.2f}%\n")
                else:
                    file.write(f"{name} - CPU: {cpu_percent:.2f}% - Memory: {memory_percent:.2f}%\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

if __name__ == "__main__":
    list_running_programs()

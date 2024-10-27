import os
import sys
import subprocess

def start_python_script(script_name):
    if os.name == 'nt': 
        subprocess.run(['python', script_name])
    else: 
        subprocess.run(['python3', script_name])

if __name__ == '__main__':
    subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])
    script_to_run = r'./scripts/main.pyw'  

    if not os.path.exists(script_to_run):
        print(f"Error: The script {script_to_run} does not exist.")
        sys.exit(1)

    start_python_script(script_to_run)

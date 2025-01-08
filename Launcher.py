print('its a whole launcher / downloader, so it will clone this repo, so delete all files before starting this, dont worry, everything will be re-downloaded anyway')
input('press a key to continue, or close the terminal to cancel')
# FAR OF BEING PERFECT, IK IT DOSENT START VAPE PROPERLY JUST START IT YOUR SELF IF IT DOSENT START AUTOMATICALLY, AT LEAST YOU WILL HAVE THE SERVER RUNNING
import os
os.system('pip install gitpython') #fixed typo pythongit -> gitpython
import sys
import subprocess
import logging
import git
import venv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clone_repository(repo_url, destination):
    try:
        git.Repo.clone_from(repo_url, destination)
        logging.info(f"Repository cloned into {destination}.")
    except Exception as e:
        logging.error(f"Error cloning repository: {e}")
        sys.exit(1)

def setup_virtual_environment(venv_folder):
    try:
        venv.create(venv_folder, with_pip=True)
        logging.info(f"Virtual environment created in {venv_folder}.")
    except Exception as e:
        logging.error(f"Error creating virtual environment: {e}")
        sys.exit(1)

def install_requirements(venv_folder, requirements_file):
    pip_executable = os.path.join(venv_folder, "Scripts", "pip.exe") if os.name == "nt" else os.path.join(venv_folder, "bin", "pip")
    try:
        subprocess.run([pip_executable, "install", "-r", requirements_file], check=True)
        logging.info("Requirements installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing requirements: {e}")
        sys.exit(1)

def get_target_folder(repo_name, version):
    folders = {
        "v4": os.path.join(repo_name, "Vape V4 Cracked"),
        "lite": os.path.join(repo_name, "Vape Lite Cracked")
    }
    return folders.get(version, None)

def start_server_in_new_terminal(venv_folder, script_name):
    activate_script = os.path.join(venv_folder, "Scripts", "activate.bat") if os.name == "nt" else os.path.join(venv_folder, "bin", "activate")
    command = f"{activate_script} && python {script_name}" if os.name != "nt" else f"cmd /c \"{activate_script} & python {script_name}\""
    try:
        subprocess.Popen(command, shell=True)
        logging.info(f"Server script {script_name} started in a new terminal.")
    except Exception as e:
        logging.error(f"Error starting server: {e}")
        sys.exit(1)

def perform_drag_and_drop(program_exe, kangaroo_exe):
    try:
        program_exe = f'"{program_exe}"'
        kangaroo_exe = f'"{kangaroo_exe}"'
        command = f'{kangaroo_exe} {program_exe}'
        full_command = f'start cmd /K {command}'
        logging.info(f"Full command to execute: {full_command}")
        subprocess.Popen(full_command, shell=True)
        logging.info(f"Executed '{program_exe}' with '{kangaroo_exe}' in a new terminal.")
    except Exception as e:
        logging.error(f"Error performing drag-and-drop action: {e}")
        sys.exit(1)

def main():
    repo_url = "https://github.com/Kolhax/Vape-V4-Crack"
    repo_name = "Vape-V4-Crack"
    try:
        clone_repository(repo_url, repo_name)
    except: pass

    version = input("Enter the version (V4/Lite): ").strip().lower()
    target_folder = get_target_folder(repo_name, version)

    if not target_folder or not os.path.isdir(target_folder):
        logging.error(f"Target folder for version '{version}' does not exist. Exiting.")
        sys.exit(1)

    os.chdir(target_folder)

    venv_folder = "venv"
    setup_virtual_environment(venv_folder)

    requirements_file = "freeze.txt"
    if not os.path.isfile(requirements_file):
        logging.error(f"{requirements_file} not found in {target_folder}. Exiting.")
        sys.exit(1)

    install_requirements(venv_folder, requirements_file)

    server_script = "server.py"
    if not os.path.isfile(server_script):
        logging.error(f"{server_script} not found in {target_folder}. Exiting.")
        sys.exit(1)

    start_server_in_new_terminal(venv_folder, server_script)

    if version == "v4":
        converted_version = 'Vape_v4'
    elif version == "lite":
        converted_version = 'Vape Lite'
    else:
        logging.error('Invalid version specified. Exiting.')
        sys.exit(1)
    
    k = converted_version.replace(" ","_")+".exe"
    
    kangaroo_exe = os.path.join(os.getcwd(), converted_version, "Kangaroo Patcher.exe")
    program_exe = os.path.join(os.getcwd(), converted_version, k)
    
    logging.info(f"Current working directory: {os.getcwd()}")
    logging.info(f"Kangaroo executable path: {kangaroo_exe}")
    logging.info(f"Program executable path: {program_exe}")

    perform_drag_and_drop(program_exe, kangaroo_exe)

    logging.info("Setup and execution complete.")

    logging.infor("Please Concideer leaving a star on my repo :D at: https://github.com/Kolhax/Vape-V4-Source")
if __name__ == "__main__":
    main()

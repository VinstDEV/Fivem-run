import os
import subprocess

def run_fivem():
    username = os.environ.get("USERNAME")
    fivem_path = f"C:/Users/{username}/AppData/Local/FiveM/FiveM.exe"
    try:
        subprocess.run([fivem_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print(e.stdout.decode())
        print(e.stderr.decode())

if __name__ == "__main__":
    run_fivem()

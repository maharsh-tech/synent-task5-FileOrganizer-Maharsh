import os
import time
from datetime import datetime
from detector import is_protected, get_category
from organizer import organize_file

def get_folder_snapshot(folder_path):
    """Returns a set of filenames currently present in the folder."""
    if not os.path.exists(folder_path):
        return set()
    try:
        return {item for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, item))}
    except Exception:
        return set()

def watch_folder(folder_path):
    """Watches the specified folder for new files in real-time."""
    print("==========================================")
    print("     👁️  WATCHDOG MODE — File Organizer")
    print("==========================================")
    print(f"Watching: {folder_path}")
    print("Interval: every 3 seconds | Ctrl+C to stop")
    print("------------------------------------------")

    old_snapshot = get_folder_snapshot(folder_path)

    try:
        while True:
            time.sleep(3)
            fresh_snapshot = get_folder_snapshot(folder_path)
            new_files = fresh_snapshot - old_snapshot
            
            # Filter out protected files
            new_files = {f for f in new_files if not is_protected(f)}
            
            if new_files:
                for filename in sorted(new_files):
                    category = get_category(filename)
                    moved = organize_file(filename, folder_path)
                    if moved:
                        timestamp = datetime.now().strftime("%H:%M:%S")
                        print(f"[{timestamp}]  {filename:20s}  ->  {category}/")
            
            old_snapshot = fresh_snapshot
    except KeyboardInterrupt:
        print("\n⛔ Stopped.")


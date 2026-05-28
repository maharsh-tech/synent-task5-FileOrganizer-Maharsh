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
    start_time = time.time()
    total_organized = 0

    try:
        while True:
            time.sleep(3)
            fresh_snapshot = get_folder_snapshot(folder_path)
            new_files = fresh_snapshot - old_snapshot
            
            # Filter out protected files
            new_files = {f for f in new_files if not is_protected(f)}
            
            unstable_files = set()
            if new_files:
                for filename in sorted(new_files):
                    full_path = os.path.join(folder_path, filename)
                    try:
                        size_1 = os.path.getsize(full_path)
                        time.sleep(1)
                        size_2 = os.path.getsize(full_path)
                        if size_1 != size_2:
                            unstable_files.add(filename)
                            continue
                    except Exception:
                        unstable_files.add(filename)
                        continue

                    category = get_category(filename)
                    moved = organize_file(filename, folder_path)
                    if moved:
                        total_organized += 1
                        timestamp = datetime.now().strftime("%H:%M:%S")
                        print(f"[{timestamp}]  {filename:20s}  ->  {category}/")
            
            old_snapshot = fresh_snapshot - unstable_files
    except KeyboardInterrupt:
        elapsed = time.time() - start_time
        if elapsed < 60:
            time_str = f"{int(elapsed)}s"
        elif elapsed < 3600:
            time_str = f"{int(elapsed // 60)}m {int(elapsed % 60)}s"
        else:
            time_str = f"{int(elapsed // 3600)}h {int((elapsed % 3600) // 60)}m {int(elapsed % 60)}s"
        
        print("------------------------------------------")
        print("⛔ Stopped.")
        print(f"📊 Session: {total_organized} file(s) organized in {time_str}")
        print("==========================================")


import os
import time
from datetime import datetime
from detector import is_protected
from organizer import organize_file

def get_folder_snapshot(folder_path):
    """Returns a set of filenames currently present in the folder."""
    if not os.path.exists(folder_path):
        return set()
    try:
        return {item for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, item))}
    except Exception:
        return set()

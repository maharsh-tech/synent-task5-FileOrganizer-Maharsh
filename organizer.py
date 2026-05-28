import os
import shutil
import logging

from detector import get_category, is_protected

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  |  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("organizer.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


def organize_file(filename, source_folder):

    file_path = os.path.join(source_folder, filename)

    # make sure its actually a file
    if not os.path.isfile(file_path):
        return False

    category = get_category(filename)

    destination_folder = os.path.join(source_folder, category)

    # Create the folder 
    os.makedirs(destination_folder, exist_ok=True)

    destination_path = os.path.join(destination_folder, filename)

    # Handle duplicate filename
    destination_path = resolve_duplicate(destination_path)

    try:
        shutil.move(file_path, destination_path)
        logging.info(f"MOVED    {filename:40s}  ->  {category}/")
        return True

    except PermissionError:
        logging.warning(f"SKIPPED  {filename:40s}  (file is in use / no permission)")
        return False

    except Exception as e:
        logging.error(f"ERROR    {filename:40s}  ({str(e)})")
        return False


def organize_folder(folder_path):

    # Check if the folder actually exists
    if not os.path.exists(folder_path):
        logging.error(f"Folder not found: {folder_path}")
        return {}

    logging.info(f"Scanning: {folder_path}")
    logging.info("-" * 60)

    summary = {}
    skipped = 0

    for item in os.listdir(folder_path):

        full_path = os.path.join(folder_path, item)

        # only handle files
        if not os.path.isfile(full_path):
            continue

        if is_protected(item):
            logging.info(f"PROTECTED  {item:40s}  (skipped)")
            skipped += 1
            continue

        category = get_category(item)
        moved    = organize_file(item, folder_path)

        if moved:
            summary[category] = summary.get(category, 0) + 1

    return summary


def resolve_duplicate(destination_path):

    if not os.path.exists(destination_path):
        return destination_path 

    folder  = os.path.dirname(destination_path)
    name, ext = os.path.splitext(os.path.basename(destination_path))

    counter = 1
    while True:
        new_path = os.path.join(folder, f"{name}_{counter}{ext}")
        if not os.path.exists(new_path):
            return new_path
        counter += 1
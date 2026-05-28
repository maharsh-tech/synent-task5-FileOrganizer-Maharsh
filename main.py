import sys

#this is wirrten by ai
# Reconfigure stdout/stderr to use UTF-8 to prevent UnicodeEncodeError on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

#upto here due to errors i had to use it

from organizer import organize_folder

def print_banner():
    print()
    print("=" * 55)
    print("File Organizer - Maharsh")
    print("=" * 55)

def print_summary(summary):

    if not summary:
        print("\n Nothing to organize, folder is already clean!")
        return
 
    total = sum(summary.values())
 
    print()
    print("-" * 40)
    print(" SUMMARY")
    print("-" * 40)

    for category, count in sorted(summary.items()):
        
        emoji = {
            "Images"   : "🖼️ ",
            "Docs"     : "📄",
            "Videos"   : "🎬",
            "Audio"    : "🎵",
            "Archives" : "📦",
            "Code"     : "💻",
            "Others"   : "❓",
        }.get(category, "📁")

        print(f"{emoji}  {category:15s}  {count} file(s)")
    
    print("-" * 40)
    print(f"Total organized: {total} file(s)")
    print("-" * 40)
    print()

def get_folder_path():

    if len(sys.argv) > 1:
        return sys.argv[1]
 
    
    print("  Enter the full path of the folder to organize.")
    print("  Example: /Users/yourname/Downloads")
    print()
    folder = input("📂 Folder path: ").strip()
 
    return folder


    

def main():
    print_banner()

    print("Select Mode:")
    print("  [1] Organize existing files now")
    print("  [2] Watch folder in real-time (Watchdog mode)")
    print()
    mode = input("Select option (1 or 2): ").strip()

    if mode not in ("1", "2"):
        print("Invalid selection. Exiting.")
        return

    folder_path = get_folder_path()
 
    if not folder_path:
        print("No folder path provided. Exiting.")
        return
 
    if mode == "1":
        print(f"\n Starting organizer on: {folder_path}")
        print()
        summary = organize_folder(folder_path)
        print_summary(summary)
    else:
        from watchdog import watch_folder
        watch_folder(folder_path)

if __name__ == "__main__":
    main()
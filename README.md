# File Organizer

A lightweight Python utility to keep folders clean and sorted. It categorizes files by extension and moves them into designated subdirectories.

It supports two modes of operation:
1. **Organize Now:** A one-time run that scans a directory and cleans it up immediately.
2. **Watchdog Mode:** A real-time folder monitor that runs in the background and automatically moves files as they are created or downloaded.

---

## Features

- **Categorized Sorting:** Automatically groups files into:
  - `Images/` (.jpg, .png, .gif, etc.)
  - `Docs/` (.pdf, .docx, .txt, etc.)
  - `Videos/` (.mp4, .mkv, .avi, etc.)
  - `Audio/` (.mp3, .wav, etc.)
  - `Archives/` (.zip, .tar, .rar, etc.)
  - `Code/` (.py, .js, .cpp, etc.)
  - `Others/` (any unrecognized extensions)
- **Real-Time Monitoring:** Checks your directory every 3 seconds for new additions.
- **Write-Safe Check:** Before moving a newly detected file, it verifies that the file size is stable (waits 1 second to make sure it's not still downloading or copying).
- **Graceful Shutdown:** Hit `Ctrl+C` in watchdog mode to stop the watcher and view a session summary of files organized and elapsed run time.
- **Safety Protections:** Skips script files (`main.py`, `detector.py`, etc.), log files, and system directories to prevent accidental self-organization.

---

## How to Run

1. Clone or download this repository.
2. Run the main entry point:
   ```bash
   python main.py
   ```
3. Select your preferred mode from the terminal menu:
   - Enter `1` to organize existing files.
   - Enter `2` to watch the folder in real-time.
4. Input the full directory path you want to organize.

---

## Project Structure

- `main.py` - Application entry point and mode selector.
- `organizer.py` - Core logic for moving files and generating sorting summaries.
- `detector.py` - Categorization rules and file path checks.
- `watchdog.py` - Directory polling, size-stability checking, and real-time watcher loop.

EXTENSION_MAP = {

    # Images
    "jpg"  : "Images",
    "jpeg" : "Images",
    "png"  : "Images",
    "gif"  : "Images",
    "bmp"  : "Images",
    "svg"  : "Images",
    "webp" : "Images",
    "ico"  : "Images",

    # Documents
    "pdf"  : "Docs",
    "doc"  : "Docs",
    "docx" : "Docs",
    "txt"  : "Docs",
    "xlsx" : "Docs",
    "xls"  : "Docs",
    "pptx" : "Docs",
    "ppt"  : "Docs",
    "csv"  : "Docs",
    "odt"  : "Docs",

    # Videos
    "mp4"  : "Videos",
    "mkv"  : "Videos",
    "avi"  : "Videos",
    "mov"  : "Videos",
    "wmv"  : "Videos",
    "flv"  : "Videos",
    "webm" : "Videos",

    # Audio
    "mp3"  : "Audio",
    "wav"  : "Audio",
    "aac"  : "Audio",
    "flac" : "Audio",
    "ogg"  : "Audio",
    "m4a"  : "Audio",

    # Archives
    "zip"  : "Archives",
    "rar"  : "Archives",
    "tar"  : "Archives",
    "gz"   : "Archives",
    "7z"   : "Archives",

    # Code
    "py"   : "Code",
    "js"   : "Code",
    "html" : "Code",
    "css"  : "Code",
    "java" : "Code",
    "cpp"  : "Code",
    "c"    : "Code",
    "json" : "Code",
    "xml"  : "Code",
    "sql"  : "Code",

}

# Files that should NEVER be touched by the organizer
PROTECTED_FILES = {
    "main.py",
    "organizer.py",
    "detector.py",
    "organizer.log",
}


def get_category(filename):

    # os.path.splitext splits "photo.jpg" to ("photo", ".jpg")
    import os
    _, ext = os.path.splitext(filename)

    # Remove the dot and make it lwercse 
    ext_clean = ext.lower().lstrip(".")

    # If no extension at all
    if not ext_clean:
        return "Others"

    return EXTENSION_MAP.get(ext_clean, "Others")


def is_protected(filename):
    return filename in PROTECTED_FILES
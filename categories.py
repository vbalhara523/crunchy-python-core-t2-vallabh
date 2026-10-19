def get_file_category(file_extension):
    """Determines the category folder name based on the file extension."""
    extensions_map = {
        ".jpg": "Images", ".png": "Images", ".jpeg": "Images",
        ".pdf": "Documents", ".txt": "Documents", ".csv": "Documents",
        ".mp4": "Videos", ".mp3": "Audio",
        ".zip": "Archives", ".tar": "Archives"
    }
    return extensions_map.get(file_extension.lower(), "Others")

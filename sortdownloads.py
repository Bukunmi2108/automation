import os
import shutil
from datetime import datetime

# Define your base and destination directories
BASE_URL = "C:\\Users\\BUNKUNMI\\Downloads"
VIDEO_URL = "C:\\Users\\BUNKUNMI\\Downloads\\Downloaded Videos"
IMAGE_URL = "C:\\Users\\BUNKUNMI\\Downloads\\Downloaded Images"
DOCUMENT_URL = "C:\\Users\\BUNKUNMI\\Downloads\\Downloaded Documents"
APP_URL = "C:\\Users\\BUNKUNMI\\Downloads\\Downloaded Applications"

def convert_date(timestamp):
    """Converts a Unix timestamp to a formatted date string."""
    d = datetime.fromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date

def ensure_directories_exist():
    """Ensures that all target directories exist."""
    for url in [VIDEO_URL, IMAGE_URL, DOCUMENT_URL, APP_URL]:
        os.makedirs(url, exist_ok=True)
        print(f"Ensured directory exists: {url}")

def organize_files():
    """
    Scans the base directory and moves files to appropriate subdirectories
    based on their file extension.
    """
    ensure_directories_exist() # Make sure destination folders are there

    print(f"\nScanning files in: {BASE_URL}\n")
    try:
        # Use scandir for potentially better performance with metadata
        for entry in os.scandir(BASE_URL):
            if entry.is_file(): # Process only files, not subdirectories
                file_name = entry.name
                original_path = entry.path

                destination_folder = None
                file_type = ""

                # Determine destination based on file extension
                if file_name.lower().endswith(('.pdf', '.docx', '.txt')):
                    destination_folder = DOCUMENT_URL
                    file_type = "document"
                elif file_name.lower().endswith(('.mp4', '.mkv', '.avi')):
                    destination_folder = VIDEO_URL
                    file_type = "video"
                elif file_name.lower().endswith(('.jpg', '.png', '.jpeg')):
                    destination_folder = IMAGE_URL
                    file_type = "image"
                elif file_name.lower().endswith(('.exe', '.msi', '.apk')):
                    destination_folder = APP_URL
                    file_type = "application"
                
                if destination_folder:
                    destination_path = os.path.join(destination_folder, file_name)
                    try:
                        shutil.move(original_path, destination_path)
                        print(f"SUCCESS: Moved '{file_name}' ({file_type}) to '{destination_folder}'")
                    except Exception as e:
                        print(f"ERROR: Could not move '{file_name}' to '{destination_folder}'. Reason: {e}")
                else:
                    print(f"INFO: '{file_name}' - No specific destination found for this file type.")
            else:
                print(f"INFO: '{entry.name}' is a directory, skipping.")

    except FileNotFoundError:
        print(f"ERROR: Base directory not found: {BASE_URL}")
    except PermissionError:
        print(f"ERROR: Permission denied to access {BASE_URL} or its subdirectories. Run script as administrator.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the file organization process
organize_files()
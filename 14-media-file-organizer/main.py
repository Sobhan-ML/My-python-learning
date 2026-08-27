import os
import time

def organize_files(source_dir: str, destination_dir: str) -> None:
    """
    Scans the source directory for photos and videos, and copies them to the 
    destination directory categorized by their modification year and file type.
    """
    PHOTO_EXTENSIONS = ['.jpg', '.jpeg', '.png']
    VIDEO_EXTENSIONS = ['.mp4', '.3gp', '.mkv', '.mov', '.wmv', '.mpeg', '.avi']

    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            filename, extension = os.path.splitext(file)
            
            # Categorize based on extension
            if extension.lower() in PHOTO_EXTENSIONS:
                folder_category = 'photos'
            elif extension.lower() in VIDEO_EXTENSIONS:
                folder_category = 'videos'
            else:
                continue  # Skip unsupported file types
            
            try:
                # Extract modification year
                modification_time = os.path.getmtime(file_path)
                year = time.ctime(modification_time).split()[-1]
                
                # Construct destination path and create folders if they don't exist
                new_folder_path = os.path.join(destination_dir, year, folder_category)
                os.makedirs(new_folder_path, exist_ok=True)
                
                final_file_path = os.path.join(new_folder_path, file)
                
                # Binary read/write process for copying the file
                with open(file_path, 'rb') as file_read:
                    data = file_read.read()

                with open(final_file_path, 'wb') as file_write:
                    file_write.write(data)
                    
                print(f"✅ Copied: {file} -> {new_folder_path}")
                
            except Exception as e:
                print(f"⚠️ Warning: Failed to process '{file}'. Reason: {e}")


def main():
    print("========================================")
    print("Welcome to the Media File Organizer! 🗂️")
    print("========================================")

    # 1. Get and validate the source directory
    while True:
        print("\nEnter the full path of the folder you want to organize (Source):")
        source_directory = input("-> ").strip()
        
        # Remove quotes in case the user dragged and dropped the folder
        source_directory = source_directory.strip('"\'')
        
        if not source_directory:
            print("❌ Error: Path cannot be empty.")
            continue
            
        if not os.path.exists(source_directory):
            print("❌ Error: Directory does not exist! Please check the path and try again.")
            continue
            
        break

    # 2. Get the destination directory
    while True:
        print("\nEnter the full path where you want the organized files to be saved (Destination):")
        destination_directory = input("-> ").strip()
        destination_directory = destination_directory.strip('"\'')
        
        if not destination_directory:
            print("❌ Error: Path cannot be empty.")
            continue
            
        break

    print("\nProcessing files... This might take a moment depending on the folder size.\n")

    organize_files(source_directory, destination_directory)

    print("\nAll files organized successfully! 🚀")


if __name__ == "__main__":
    main()
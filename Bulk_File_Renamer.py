import os

def bulk_rename_files(directory, new_base_name):
    """
    Renames all image files in a specified directory to a consistent,
    numbered pattern while preserving their original extensions.

    Args:
        directory (str): The file path to the folder containing images.
        new_base_name (str): The new base name for the files (e.g., "product").
    """
    
    image_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp', '.tiff')
    
    counter = 1

    print(f"--- Starting bulk rename in folder: {directory} ---")

    try:
        all_files = os.listdir(directory)
        
        all_files.sort()

        for filename in all_files:
         
            file_ext = os.path.splitext(filename)[1]
            
            if file_ext.lower() in image_extensions:
               
                new_filename = f"{new_base_name}_{counter:03d}{file_ext}"

                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)

                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: '{filename}'  ->  '{new_filename}'")
                    
                    counter += 1
                
                except OSError as e:
                    print(f"Error renaming {filename}: {e}")
                    
            else:
                print(f"Skipped:  '{filename}' (not a recognized image)")

        print(f"\n--- Bulk rename complete. {counter - 1} files renamed. ---")

    except FileNotFoundError:
        print(f"Error: The directory '{directory}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

TARGET_FOLDER = os.path.dirname(os.path.abspath(__file__))
NEW_PREFIX = "indikraft_product"

bulk_rename_files(TARGET_FOLDER, NEW_PREFIX)
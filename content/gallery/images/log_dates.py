import os
from PIL import Image
from datetime import datetime

# The numeric tag ID for the "DateTime"
TAG_DATE_TIME = 306

def get_exif_date(filepath):
    try:
        img = Image.open(filepath)
        exif_data = img._getexif()

        if exif_data:
            # Returns a string like '2025:11:08 15:30:00'
            date_str = exif_data.get(TAG_DATE_TIME) 
            return date_str
    except Exception:
        return None
    return None

def rename_files_in_directory(directory="."):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue

            filepath = os.path.join(root, file)
            date_str = get_exif_date(filepath)
            
            if date_str:
                try:
                    # 1. Parse the EXIF date string
                    #    Format is 'YYYY:MM:DD HH:MM:SS'
                    dt = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
                    
                    # 2. Format it to your desired prefix
                    prefix = dt.strftime('%Y-%m-%d')
                    
                    # 3. Create the new name
                    new_filename = f"{prefix}-{file}"
                    
                    # 4. Check if it's already renamed
                    if file.startswith(prefix):
                        print(f"Skipped (already renamed): {file}")
                        continue
                        
                    # 5. Rename the file
                    new_filepath = os.path.join(root, new_filename)
                    os.rename(filepath, new_filepath)
                    print(f"Renamed: {file} -> {new_filename}")

                except Exception as e:
                    print(f"Error processing {file}: {e}")

# --- Run the script ---
if __name__ == "__main__":
    print("Starting rename process...")
    # Be careful! This runs in the script's current directory.
    rename_files_in_directory(".") 
    print("Done.")
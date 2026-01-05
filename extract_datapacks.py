import os
import zipfile

start_underscore = 3

def process_zip_folders(main_folder_path):
    processed = 0
    for item in os.listdir(main_folder_path):
        if item.lower().endswith('.zip'):
            zip_path = os.path.join(main_folder_path, item)
            
            # Get filename without extension
            name_without_ext = os.path.splitext(item)[0]
            
            parts = name_without_ext.split('_')
            if len(parts) >= 4:
                version = parts[start_underscore]
            else:
                print(f"Skipping {item}: not enough underscores (found {len(parts)} parts)")
                continue
            
            # Create extraction folder in main folder
            extract_folder = os.path.join(main_folder_path, version)
            os.makedirs(extract_folder, exist_ok=True)
            
            # Extract zip to the folder
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
            
            print(f"✓ Extracted {item} to {version}/")
            processed += 1
    
    print(f"\nProcessed {processed} zip files.")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Processing zips in: {script_dir}")
    process_zip_folders(script_dir)
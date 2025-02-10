import os
import shutil
import sys
import time

def backup_files(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")

    if not os.path.exists(destination_dir):
        print(f"Destination directory '{destination_dir}' does not exist. Creating it...")
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        

        if os.path.isfile(source_file):
            destination_file = os.path.join(destination_dir, filename)


            if os.path.exists(destination_file):
                timestamp = time.strftime("%Y%m%d%H%M%S")
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{timestamp}{ext}"
                destination_file = os.path.join(destination_dir, new_filename)

            shutil.copy2(source_file, destination_file)
            print(f"Copied: {filename} -> {destination_file}")

    print("\nBackup completed successfully!")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    backup_files(source_directory, destination_directory)

import os
import shutil

# Define the target folder and tags
target_folder = "/home/ray/Documents/ECE/2.2/"
directory_tags = {
    "Analogue Elec": ["Analogue","Analogue Elec", "Analogue Electronics", "EEE 2210", "2210"],
    "CNT": ["CNT"],
    "Electrical Machines": ["tag4"],
    "ElectroMagnetism": ["tag5"],
    "Mech Principles": ["tag6"],
    "ODE": ["tag7"],
    "OS": ["tag8"],
    "Phy Elec": ["tag9"]
}

# Define the downloads folder
downloads_folder = "/home/ray/Downloads/"

# Iterate over the files in the downloads folder
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    # Check if it's a file and not a subdirectory
    if os.path.isfile(file_path):
        # Check if the file name contains any of the specified tags
        matching_directories = [directory for directory, tags in directory_tags.items() if any(tag in filename for tag in tags)]

        # If there are matching directories, copy the file to each respective directory in the target folder
        if matching_directories:
            for directory in matching_directories:
                target_directory = os.path.join(target_folder, directory)

                # Create the target directory if it doesn't exist
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)

                # Check if the file already exists in the target directory
                if not os.path.exists(os.path.join(target_directory, filename)):
                    # Move the file to the target directory
                    shutil.move(file_path, target_directory)
                    print(f"File '{filename}' moved to '{target_directory}'.")
                else:
                    print(f"File '{filename}' already exists in '{target_directory}'. Skipping.")

        # If there are no matching tags, move the file to a default subdirectory in the target folder
        else:
            default_folder = os.path.join(target_folder, "default")

            # Create the default folder if it doesn't exist
            if not os.path.exists(default_folder):
                os.makedirs(default_folder)

            # Check if the file already exists in the default folder
            if not os.path.exists(os.path.join(default_folder, filename)):
                shutil.move(file_path, default_folder)
                print(f"File '{filename}' moved to '{default_folder}'.")
            else:
                print(f"File '{filename}' already exists in '{default_folder}'. Skipping.")

                # Move the file to the target directory
                shutil.move(file_path, target_directory)
                print(f"File '{filename}' moved to '{target_directory}'.")

                # Optionally, you can delete the file from the downloads folder after moving
                # os.remove(file_path)

                # If there are no matching tags, move the file to a default subdirectory in the target folder
        
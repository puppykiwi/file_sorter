import os
import time
import shutil

# Define the target folder and tags
target_folder = "/home/ray/Documents/ECE/2.2/"
directory_tags = {
    "Analogue Elec": ["Analogue","Analogue Elec", "Analogue Electronics", "EEE 2210", "2210"],
    "CNT": ["2213", "EEE 2213 CIRCUIT AND NETWORK THEORY", "Circuit and Network Theory", "EEE 2213", "CNT", "Circuit", "Network", "EEE2213", "2213", "Circuit Theory"],
    "Electrical Machines": ["2214", "EEE 2214 ELECTRICAL MACHINES", "Electrical Machines", "EEE 2214", "EEE2214", "Machines", "EEE2214 Electrical Machines", "EEE 2214 Machines", "EEE 2214 EM", "EEE 2214 Elec Machines", "EEE 2214 EMachines"],
    "ElectroMagnetism": ["2215", "EEE 2215 ELECTROMAGNETICS", "Electromagnetics", "EEE 2215 EM", "EEE 2215 ElecMag", "EEE 2215 Electromag", "EEE 2215 Electromagnetic Theory", "EEE2215", "2215", "Electromagnetic Field Theory", "Electromagnetic Waves"],
    "Mech Principles": ["2211", "EME 2211", "MECHANICAL ENGINEERING PRINCIPLES", "EME 2211 MECHANICAL ENGINEERING PRINCIPLES", "MECHANICAL PRINCIPLES", "MECHANICAL ENG PRINCIPLES", "EME 2211 MECH ENG PRINCIPLES", "MECH ENG PRINCIPLES", "MECH PRINCIPLES", "EME 2211 MECH PRINCIPLES", "MECHANICAL ENGINEERING"],
    "ODE": ["2271","SMA 2271 ORDINARY DIFFERENTIAL EQUATIONS", "ODE", "SMA 2271", "SMA2271", "Ordinary Differential Equations", "Differential Equations", "Mathematical Methods"],
    "OS": ["2270","ICS", "ICS 2270 OPERATING SYSTEMS", "Operating Systems", "ICS 2270 OS", "ICS 2270", "Operating System", "OS", "ICS2270", "2270", "ICS 2270 Operating Systems", "ICS 2270 Operating System"],
    "Phy Elec": ["2212","EEE 2212 PHYSICAL ELECTRONICS", "EEE 2212 Physical Electronics", "EEE2212", "2212", "Physical Electronics", "EEE2212 Phy Elec", "EEE 2212 Phy Elec", "EEE 2212 PE", "EEE 2212 Phys Elec", "EEE 2212 Physical Elec"]
}

# Define the downloads folder
downloads_folder = "/home/ray/Downloads/"
check_interval = 5 # seconds

while True:
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

    # Wait for the specified interval before checking again
    time.sleep(check_interval)
        

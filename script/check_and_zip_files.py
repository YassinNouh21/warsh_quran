import os
import zipfile

# Directory containing the SVGZ files
directory = 'svgzs'

# Check if the directory exists
if not os.path.exists(directory):
    print(f"Directory '{directory}' does not exist.")
    exit(1)

# Get a list of files in the directory
files = os.listdir(directory)

# Filter out non-file entries (like directories) and ensure we only consider .svgz files
files = [file for file in files if os.path.isfile(os.path.join(directory, file)) and file.endswith('.svgz')]

# Extract file numbers from filenames assuming they are in the format 'number.svgz'
file_numbers = []
for file in files:
    try:
        # Extract the number part from the filename
        number = int(os.path.splitext(file)[0])
        file_numbers.append(number)
    except ValueError:
        print(f"Skipping file with non-numeric name: {file}")
        continue

# Check for missing files in the sequence 1 to 604
missing_files = []
for i in range(1, 605):
    if i not in file_numbers:
        missing_files.append(i)

# Print the results and proceed to zip if there are no missing files
if not missing_files:
    print("All files from 1 to 604 are present. Proceeding to zip them.")
    
    # Create a ZIP file
    zip_filename = 'svgzs.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in sorted(files, key=lambda x: int(os.path.splitext(x)[0])):
            zipf.write(os.path.join(directory, file), arcname=file)
    
    print(f"All files have been zipped into {zip_filename}.")
else:
    print("The following files are missing:")
    print(missing_files)
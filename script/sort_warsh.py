import os

# Directory containing the SVGZ files
directory = 'svgzs'

# Check if the directory exists
if not os.path.exists(directory):
    print(f"Directory '{directory}' does not exist.")
    exit(1)

# Get a list of files in the directory
files = os.listdir(directory)

# Filter out non-file entries (like directories)
files = [file for file in files if os.path.isfile(os.path.join(directory, file))]

# Sort files by name
sorted_files = sorted(files, key=lambda x: x.lower())  # Case-insensitive sorting

# Print sorted files
print("Sorted files by name:")
for file in sorted_files:
    print(file)
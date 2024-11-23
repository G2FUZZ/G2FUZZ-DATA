import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'ras' files with the specified features
features = "6. Resolution: Can store resolution information for the image."
file_content = f"Features of the ras file:\n{features}"

for i in range(3):
    file_name = f"{directory}file_{i + 1}.ras"
    with open(file_name, 'w') as file:
        file.write(file_content)

print("Files generated successfully.")
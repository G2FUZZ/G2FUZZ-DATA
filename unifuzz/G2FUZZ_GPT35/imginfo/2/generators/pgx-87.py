import os
import random
import string
import datetime

# Define the features for the 'pgx' files with additional complexity
features = {
    "Version compatibility": "Version information to ensure compatibility with specific software or hardware.",
    "File size": "Size of the file in bytes.",
    "Creation date": "Date and time when the file was created."
}

# Create a directory to store the 'pgx' files
directory = './tmp'
os.makedirs(directory, exist_ok=True)

# Generate 'pgx' files with the defined features
for i, (feature, description) in enumerate(features.items(), start=1):
    file_name = f"{directory}/file_{i}.pgx"
    with open(file_name, 'w') as file:
        if feature == "File size":
            file_size = random.randint(100, 1000)  # Random file size between 100 and 1000 bytes
            file.write(f"Feature: {feature}\nDescription: {description}\nFile Size: {file_size} bytes")
        elif feature == "Creation date":
            creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Feature: {feature}\nDescription: {description}\nCreation Date: {creation_date}")
        else:
            file.write(f"Feature: {feature}\nDescription: {description}")

    print(f"'{file_name}' generated with feature: '{feature}'")

print("Files saved in './tmp/' directory.")
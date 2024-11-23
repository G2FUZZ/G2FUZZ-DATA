import os

# Ensure the directory exists
os.makedirs('./tmp/', exist_ok=True)

# Features to write to the mp3 file
feature1 = "Wide compatibility: MP3 files are supported by a wide range of devices and audio players."
feature2 = "Embedded scripts: MP3 files can contain embedded scripts or executable code for interactive audio applications or enhanced functionality."

# Concatenate the features
features = f"{feature1}\n\n{feature2}"

# Write the features to an mp3 file
file_path = "./tmp/feature_extended.mp3"
with open(file_path, 'w') as file:
    file.write(features)

print(f"MP3 file with the extended features has been generated and saved at: {file_path}")
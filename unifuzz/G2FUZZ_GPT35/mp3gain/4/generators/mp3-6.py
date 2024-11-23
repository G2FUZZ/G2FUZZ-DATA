import os

# Ensure the directory exists
os.makedirs('./tmp/', exist_ok=True)

# Feature to write to the mp3 file
feature = "Wide compatibility: MP3 files are supported by a wide range of devices and audio players."

# Write the feature to an mp3 file
file_path = "./tmp/feature.mp3"
with open(file_path, 'w') as file:
    file.write(feature)

print(f"MP3 file with the feature has been generated and saved at: {file_path}")
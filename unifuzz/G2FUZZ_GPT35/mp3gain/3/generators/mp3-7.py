import os

# Create a directory if it doesn't exist
os.makedirs("./tmp/", exist_ok=True)

# Generate an 'mp3' file with the specified feature
with open("./tmp/mp3_feature.txt", "w") as file:
    file.write("Compatibility: MP3 files are widely supported by various devices and software applications for playback and sharing.")
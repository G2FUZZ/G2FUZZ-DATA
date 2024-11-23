import os

# Ensure the directory exists
os.makedirs('./tmp/', exist_ok=True)

# Features
features = [
    "Wide compatibility: MP3 files are supported by a wide range of devices and audio players.",
    "Lyrics support: Some MP3 files may contain embedded lyrics that can be displayed by compatible media players.",
    "ReplayGain: MP3 files can support ReplayGain information for volume normalization during playback."
]

# Write the features to an mp3 file
file_path = "./tmp/extended_feature.mp3"
with open(file_path, 'w') as file:
    for feature in features:
        file.write(feature + '\n')

print(f"MP3 file with the extended features has been generated and saved at: {file_path}")
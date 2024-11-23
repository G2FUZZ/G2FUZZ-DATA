import os
import json

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ani' file with advanced features
ani_file_path = './tmp/complex_animation_with_audio.ani'

# Define animation content
animation_content = "Complex Animation Content"
audio_tracks = ["Audio Track 1", "Audio Track 2"]
metadata = {
    "title": "Complex Animation with Multiple Audio Tracks",
    "author": "John Doe",
    "duration": "5 minutes"
}

# Write to the ani file
with open(ani_file_path, 'w') as ani_file:
    ani_file.write("Animation Content: " + animation_content + "\n")
    ani_file.write("Metadata: " + json.dumps(metadata) + "\n")
    ani_file.write("Audio Tracks:\n")
    for track in audio_tracks:
        ani_file.write("- " + track + "\n")

print(f"'ani' file with advanced features generated at: {ani_file_path}")
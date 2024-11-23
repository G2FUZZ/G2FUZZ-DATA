import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate dummy mp3 file with joint stereo and constant quality mode features
mp3_data = b'\xFF\xFB\x90\x00\xC0'  # Dummy mp3 data with constant quality mode feature
mp3_filename = './tmp/constant_quality_mode_example.mp3'

with open(mp3_filename, 'wb') as file:
    file.write(mp3_data)

print(f"'{mp3_filename}' file with constant quality mode feature has been generated.")
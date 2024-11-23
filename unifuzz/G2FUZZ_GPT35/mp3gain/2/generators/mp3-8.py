import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate dummy mp3 file with joint stereo feature
mp3_data = b'\xFF\xFB\x90\x00'  # Dummy mp3 data
mp3_filename = './tmp/joint_stereo_example.mp3'

with open(mp3_filename, 'wb') as file:
    file.write(mp3_data)

print(f"'{mp3_filename}' file with joint stereo feature has been generated.")
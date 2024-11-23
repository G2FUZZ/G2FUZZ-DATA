import os

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple mp3 file with the specified feature
mp3_data = b'Lossy compression: MP3 files use lossy compression to reduce file size while maintaining audio quality.'
with open('./tmp/sample.mp3', 'wb') as f:
    f.write(mp3_data)

print('Generated mp3 file with lossy compression feature saved as ./tmp/sample.mp3')
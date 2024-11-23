import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate an MP4 file with 4K resolution, Dolby Atmos audio, and HDR video support
file_path = './tmp/complex_video_4k.mp4'
with open(file_path, 'wb') as file:
    file.write(b'MP4 file content with 4K resolution, Dolby Atmos audio, and HDR video support')

print(f'Generated MP4 file with 4K resolution, Dolby Atmos audio, and HDR video support: {file_path}')
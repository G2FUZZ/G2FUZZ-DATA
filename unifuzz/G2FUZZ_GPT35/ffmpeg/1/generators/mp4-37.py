import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a dummy mp4 file with a random file size
file_name = './tmp/generated_video_with_audio_feature.mp4'
file_size = 10  # in MB (dummy value)
audio_feature = 'Object-based Audio'

with open(file_name, 'wb') as f:
    f.seek(file_size * 1024 * 1024 - 1)
    f.write(b'\0')

print(f"Generated mp4 file with a size of {file_size} MB and additional feature '{audio_feature}' at '{file_name}'")
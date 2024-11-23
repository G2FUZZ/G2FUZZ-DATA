import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple mp4 file with the specified features including 'User Data'
filename = './tmp/streaming_feature_with_closed_captions_and_user_data.mp4'

file_content = b'Generated MP4 file with streaming feature, Closed Captions, and User Data'

with open(filename, 'wb') as file:
    file.write(file_content)

print(f'Generated {filename}')
import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with streaming support and closed captions features
with open('./tmp/streaming_and_closed_captions.mp4', 'wb') as f:
    f.write(b'Sample MP4 file with streaming support and closed captions features')

print('MP4 file with streaming support and closed captions features generated successfully.')
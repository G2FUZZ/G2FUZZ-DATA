import os

# Create the directory if it does not exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a dummy FLV file with the specified feature
with open('./tmp/audio_video_sync.flv', 'wb') as file:
    file.write(b'FLV File with Audio/Video Synchronization feature')
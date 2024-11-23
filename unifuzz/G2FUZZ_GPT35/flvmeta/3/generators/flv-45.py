import os

# Create the directory if it does not exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a more complex FLV file with multiple audio and video tracks, metadata, and timestamp synchronization
with open('./tmp/complex_flv_file.flv', 'wb') as file:
    # Write video data
    file.write(b'Video Track 1 Data')
    
    # Write audio data for track 1
    file.write(b'Audio Track 1 Data')
    
    # Write video data for track 2
    file.write(b'Video Track 2 Data')
    
    # Write audio data for track 2
    file.write(b'Audio Track 2 Data')
    
    # Write metadata information
    file.write(b'Metadata: Duration=10s, Resolution=1920x1080')
    
    # Write timestamps for synchronization
    file.write(b'Timestamps: Video1=0s, Audio1=0s, Video2=5s, Audio2=5s')
import os
from mutagen.mp4 import MP4

# Specify the file path
file_path = './tmp/metadata_example.mp4'

# Check if the file exists
if os.path.exists(file_path):
    # Create a new MP4 file
    mp4_file = MP4(file_path)

    # Add metadata to the file
    mp4_file['\xa9nam'] = 'Song Title'
    mp4_file['\xa9ART'] = 'Artist Name'
    mp4_file['\xa9alb'] = 'Album Name'
    mp4_file['\xa9gen'] = 'Genre'
    
    # Add HDR support feature
    mp4_file['\xa9HDR'] = 'High dynamic range (HDR) support'

    # Add multiple audio tracks
    mp4_file['trkn'] = [(1, 1)]  # Track number
    mp4_file['disk'] = [(1, 1)]  # Disk number
    mp4_file.save()
else:
    print(f"Error: File '{file_path}' does not exist.")
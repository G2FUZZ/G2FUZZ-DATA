import os

# Define the data for the FLV file with Audio, Video, and Metadata
file_data_complex = b'FLV File with Audio, Video, and Metadata'

# Define audio data
audio_data = b'Audio Data'

# Define video data
video_data = b'Video Data'

# Define metadata headers
metadata_headers = b'Metadata Headers'

# Create a directory to save the FLV files if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Write the FLV file with Audio, Video, and Metadata
with open('./tmp/file_complex_structure.flv', 'wb') as f:
    f.write(file_data_complex)
    f.write(audio_data)
    f.write(video_data)
    f.write(metadata_headers)
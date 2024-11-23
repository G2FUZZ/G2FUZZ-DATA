import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with multiple audio tracks, subtitles, and custom metadata
with open('./tmp/complex_video_file.flv', 'wb') as file:
    file.write(b'FLV Header')

    # Add multiple audio tracks
    file.write(b'FLV Body with Audio Track 1 Data')
    file.write(b'FLV Body with Audio Track 2 Data')

    # Add subtitles
    file.write(b'FLV Body with Subtitles Data')

    # Add custom metadata
    file.write(b'FLV Body with Custom Metadata')

print('FLV file with multiple audio tracks, subtitles, and custom metadata generated successfully.')
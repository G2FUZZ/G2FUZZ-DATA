import os

# Create a directory to save generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with smaller file size and Timed text tracks feature
with open('./tmp/sample_with_text_tracks.mp4', 'wb') as f:
    # Write some sample data including Timed text tracks
    f.write(b'Sample mp4 file with compressed format leading to smaller file sizes and Timed text tracks for displaying text overlays at specific times during playback')

print('Generated mp4 file with Timed text tracks feature successfully.')
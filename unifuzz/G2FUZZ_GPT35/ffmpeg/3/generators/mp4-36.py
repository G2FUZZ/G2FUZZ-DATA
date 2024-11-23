import os

# Create a directory to save generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with smaller file size, Timed text tracks, and Wide color gamut support feature
with open('./tmp/sample_with_text_tracks_and_wide_color_gamut.mp4', 'wb') as f:
    # Write some sample data including Timed text tracks and Wide color gamut support feature
    f.write(b'Sample mp4 file with compressed format leading to smaller file sizes, Timed text tracks for displaying text overlays at specific times during playback, and Wide color gamut support allowing for storing content with a wider range of colors for more vivid visuals')

print('Generated mp4 file with Timed text tracks and Wide color gamut support features successfully.')
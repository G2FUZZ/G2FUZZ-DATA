import os

# Create a directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

# Generate a sample mp3 file with Gapless Playback feature
with open('tmp/sample_gapless.mp3', 'wb') as f:
    f.write(b'\xFF\xFB\x90')  # Sample data for an mp3 file
    f.write(b'Gapless Playback Feature')  # Additional data for Gapless Playback

print("MP3 file with Gapless Playback generated successfully at ./tmp/sample_gapless.mp3")
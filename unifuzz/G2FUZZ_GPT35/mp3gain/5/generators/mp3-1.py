import os

# Create a directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

# Generate a sample mp3 file
with open('tmp/sample.mp3', 'wb') as f:
    f.write(b'\xFF\xFB\x90')  # Sample data for an mp3 file

print("MP3 file generated successfully at ./tmp/sample.mp3")
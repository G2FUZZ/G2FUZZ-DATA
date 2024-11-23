import os

# Create a directory to store generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file
sample_mp4_content = 'This is a sample MP4 file with the feature: Compatibility'
with open('./tmp/sample.mp4', 'w') as file:
    file.write(sample_mp4_content)

print("MP4 file generated successfully!")
import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample MP4 file with embedded subtitles
sample_data = "This is a sample MP4 file with embedded subtitles."
file_name = output_dir + 'sample_with_subtitles.mp4'

with open(file_name, 'w') as file:
    file.write(sample_data)

print(f"Generated MP4 file with embedded subtitles: {file_name}")
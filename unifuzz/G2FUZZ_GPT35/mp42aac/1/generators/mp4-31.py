import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with more complex features
sample_data = b'Fake MP4 data with Timed Metadata, HDR video support, Dolby Atmos audio, and Custom Video Resolutions'
file_path = './tmp/sample_extended_mp4_file.mp4'

with open(file_path, 'wb') as file:
    file.write(sample_data)

# Generate timed metadata file
timed_metadata_data = b'Timed Metadata for the mp4 file'
timed_metadata_file_path = './tmp/sample_timed_metadata.xml'

with open(timed_metadata_file_path, 'wb') as timed_metadata_file:
    timed_metadata_file.write(timed_metadata_data)

print(f"Generated a more complex MP4 file with Timed Metadata, HDR video support, Dolby Atmos audio, and Custom Video Resolutions: {file_path}")
print(f"Timed Metadata file: {timed_metadata_file_path}")
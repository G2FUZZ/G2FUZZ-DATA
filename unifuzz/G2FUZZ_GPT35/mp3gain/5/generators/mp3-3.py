import os

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp3 file with a constant bitrate of 128 kbps
sample_data = b'Fake mp3 data with constant bitrate of 128 kbps'
with open('./tmp/sample_constant_bitrate_128kbps.mp3', 'wb') as f:
    f.write(sample_data)

# Generate another sample mp3 file with a variable bitrate (e.g., ranging from 64 kbps to 192 kbps)
sample_data = b'Fake mp3 data with variable bitrate'
with open('./tmp/sample_variable_bitrate_64_192kbps.mp3', 'wb') as f:
    f.write(sample_data)
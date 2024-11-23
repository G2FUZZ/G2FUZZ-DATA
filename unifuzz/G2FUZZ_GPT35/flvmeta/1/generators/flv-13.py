import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample FLV file with the specified features
file_content = """
FLV files support streaming for progressive download and real-time streaming applications.
Multi-bitrate streaming: FLV files can be encoded with multiple bitrates for adaptive streaming to accommodate varying network conditions.
"""

file_path = os.path.join(output_dir, 'sample_multibitrate.flv')
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"FLV file with Multi-bitrate streaming feature generated successfully at: {file_path}")
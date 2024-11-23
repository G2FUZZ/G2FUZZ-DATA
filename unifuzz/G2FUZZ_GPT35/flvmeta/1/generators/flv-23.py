import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample FLV file with the specified features
file_content = """
FLV files support streaming for progressive download and real-time streaming applications.
Multi-bitrate streaming: FLV files can be encoded with multiple bitrates for adaptive streaming to accommodate varying network conditions.
Interactive features: FLV files can support interactive features such as clickable areas, menus, and user interactions.
Metadata injection: FLV files can allow for metadata injection during encoding or post-processing to add information such as copyright details or keywords.
"""

file_path = os.path.join(output_dir, 'sample_multibitrate_interactive_metadata.flv')
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"FLV file with Multi-bitrate streaming, Interactive features, and Metadata injection generated successfully at: {file_path}")
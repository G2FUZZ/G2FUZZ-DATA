import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample FLV file with multiple video tracks and metadata
file_content = """
FLV files support streaming for progressive download and real-time streaming applications.
Multiple video tracks: FLV files may contain multiple video tracks for different camera angles or resolutions.
Metadata information: FLV files can store metadata such as title, description, and creation date.
Timestamps: FLV files use timestamps to synchronize audio, video, and metadata.
"""
file_path = os.path.join(output_dir, 'sample_with_complex_structure.flv')
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"FLV file with complex file structure generated successfully at: {file_path}")
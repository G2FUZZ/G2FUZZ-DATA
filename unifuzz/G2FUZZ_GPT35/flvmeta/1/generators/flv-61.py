import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample FLV file with advanced features
file_content = """
FLV files can contain video encoded with codecs like H.264, VP6, or VP8.
Audio in FLV files can be encoded with AAC, MP3, or Nellymoser.
FLV files support metadata tags for information like duration, cue points, and script data.
"""

file_path = os.path.join(output_dir, 'sample_advanced.flv')
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"FLV file with advanced features generated successfully at: {file_path}")
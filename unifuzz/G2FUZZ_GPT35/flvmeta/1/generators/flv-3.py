import os
import random

# Generate random data for the FLV file
audio_codecs = ['AAC', 'MP3']
selected_codec = random.choice(audio_codecs)

file_content = f"FLV file with audio codec: {selected_codec}"

# Save the generated FLV file
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, 'generated_file.flv')

with open(file_path, 'w') as f:
    f.write(file_content)

print(f"FLV file with audio codec '{selected_codec}' has been generated and saved at: {file_path}")
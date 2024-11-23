import os
import random

# Generate random data for the FLV file
audio_codecs = ['AAC', 'MP3']
selected_codec = random.choice(audio_codecs)
user_data = "User data: Additional information or settings"

file_content = f"FLV file with audio codec: {selected_codec}\n{user_data}"

# Save the generated FLV file
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, 'generated_file_with_user_data.flv')

with open(file_path, 'w') as f:
    f.write(file_content)

print(f"FLV file with audio codec '{selected_codec}' and User data has been generated and saved at: {file_path}")
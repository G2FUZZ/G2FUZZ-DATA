import os
import random

# Generate random data for the FLV file
audio_codecs = ['AAC', 'MP3']
video_codecs = ['H.264', 'VP9']
selected_audio_codec = random.choice(audio_codecs)
selected_video_codec = random.choice(video_codecs)
user_data = "User data: Additional information or settings"

# Simulate timestamps for the FLV file
timestamps = [0.0, 1.5, 3.2, 4.8, 6.1]

# Construct the FLV file content with audio and video codec information
file_content = f"FLV file with audio codec: {selected_audio_codec}\n"
file_content += f"FLV file with video codec: {selected_video_codec}\n"
file_content += f"{user_data}\n"

file_content += "Timestamps:\n"
for timestamp in timestamps:
    file_content += f"{timestamp} sec\n"

# Save the generated FLV file
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, 'extended_generated_file.flv')

with open(file_path, 'w') as f:
    f.write(file_content)

print(f"Extended FLV file with audio codec '{selected_audio_codec}', video codec '{selected_video_codec}', and User data has been generated and saved at: {file_path}")
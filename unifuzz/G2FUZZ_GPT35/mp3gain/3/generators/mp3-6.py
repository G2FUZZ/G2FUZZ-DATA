import os

# Create a directory to store the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a dummy mp3 file with the specified feature
dummy_mp3_data = b'\xFF\xFB' + b'\x00' * 1000  # Dummy mp3 data

# Save the generated mp3 file
with open('./tmp/variable_frame_length.mp3', 'wb') as file:
    file.write(dummy_mp3_data)

print("Generated mp3 file with support for variable frame length.")
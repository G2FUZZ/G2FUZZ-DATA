import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample MPEG-4 file with Encryption feature
sample_data_with_encryption = b'\x00\x00\x00\x18ftypisom\x00\x00\x02\x00isomiso2mp41Encryption'
with open('./tmp/sample_encrypted.mp4', 'wb') as file:
    file.write(sample_data_with_encryption)

print("Generated 'mp4' files with Encryption feature saved in './tmp/' directory.")
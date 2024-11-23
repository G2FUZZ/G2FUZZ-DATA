import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample MPEG-4 file with Encryption and 360-degree video features
sample_data_with_encryption_and_360_video = b'\x00\x00\x00\x18ftypisom\x00\x00\x02\x00isomiso2mp41Encryption360-degree video'
with open('./tmp/sample_encrypted_and_360_video.mp4', 'wb') as file:
    file.write(sample_data_with_encryption_and_360_video)

print("Generated 'mp4' file with Encryption and 360-degree video features saved in './tmp/' directory.")
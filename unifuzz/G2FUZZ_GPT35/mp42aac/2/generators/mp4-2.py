import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample MPEG-4 file
sample_data = b'\x00\x00\x00\x18ftypisom\x00\x00\x02\x00isomiso2mp41'
with open('./tmp/sample.mp4', 'wb') as file:
    file.write(sample_data)

print("Generated 'mp4' files saved in './tmp/' directory.")
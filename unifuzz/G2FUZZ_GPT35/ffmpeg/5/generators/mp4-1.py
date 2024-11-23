import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file
with open('./tmp/sample.mp4', 'wb') as f:
    f.write(b'\x00\x00\x00\x18ftypisom\x00\x00\x02\x00isomiso2mp41\x00\x00\x00\x08free')
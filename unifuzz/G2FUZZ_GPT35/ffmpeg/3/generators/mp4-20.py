import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with Variable frame rate (VFR) support and Custom metadata
custom_metadata = b'Custom metadata: Allows for embedding custom metadata within the file for various purposes'

with open('./tmp/sample_vfr_custom_metadata.mp4', 'wb') as f:
    f.write(b'\x00\x00\x00\x20\x66\x74\x79\x70\x6d\x70\x34\x32\x00\x00\x02\x00\x69\x73\x6f\x6d\x69\x73\x6f\x32\x61\x76\x63\x31\x00\x00\x00\x28\x64\x61\x74\x61\x6d\x64\x68\x65\x76\x63\x63\x6f\x6f\x6b\x6f\x6f\x6c\x63\x6f\x6f\x6c\x6f\x76\x66\x74\x79\x70\x6d\x70\x34\x32\x69\x73\x6f\x6d\x69\x73\x6f\x32\x61\x76\x63\x31\x20\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' + custom_metadata)
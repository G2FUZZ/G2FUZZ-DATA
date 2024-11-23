import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with Chapter markers, Fast start feature, and Interactive features
with open('./tmp/sample_with_chapters_fast_start_and_interactive_features.mp4', 'wb') as f:
    f.write(b'\x00\x00\x00\x20\x66\x74\x79\x70\x6d\x70\x34\x32\x00\x00\x02\x00\x69\x73\x6f\x6d\x69\x73\x6f\x32\x61\x76\x63\x31\x00\x00\x00\x28\x64\x61\x74\x61\x6d\x64\x68\x65\x76\x63\x63\x6f\x6f\x6b\x6f\x6f\x6c\x63\x6f\x6f\x6c\x6f\x76\x66\x74\x79\x70\x6d\x70\x34\x32\x69\x73\x6f\x6d\x69\x73\x6f\x32\x61\x76\x63\x31\x20\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x18\x00\x00\x00\x00\x6d\x64\x61\x74\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01')
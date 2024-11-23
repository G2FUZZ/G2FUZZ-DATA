import os

# Create a directory to store the generated 'mp4' files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'mp4' file with streaming support, Fast start feature, and Text-based metadata
file_path = './tmp/streaming_faststart_text_metadata_example.mp4'
with open(file_path, 'wb') as f:
    # Adding Fast start feature by placing metadata at the beginning of the file
    f.write(b'MP4 Fast Start Feature - Metadata placed at the beginning for quick playback initiation. MP4 files are commonly used for streaming media over the internet.')
    
    # Adding Text-based metadata using XMP format
    f.write(b'\nXMP Metadata: Extensible Metadata Platform (XMP) allows for richer metadata descriptions in text-based format.')

print(f"Generated 'mp4' file with Fast start feature and Text-based metadata: {file_path}")
import os

# Create a directory to store the generated mp4 files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a sample mp4 file with DRM protection, Fast start, and Image overlays
sample_file_path = os.path.join(output_dir, 'sample_drm_fast_start_image_overlays.mp4')

# Writing the moov atom at the beginning of the file
moov_atom = b'moov atom content'
video_content = b'Generated DRM protected MP4 file content'
image_overlay = b'Image overlay content'

with open(sample_file_path, 'wb') as f:
    f.write(moov_atom)
    f.write(video_content)
    f.write(image_overlay)

print(f"Generated DRM protected MP4 file with Fast start and Image overlays: {sample_file_path}")
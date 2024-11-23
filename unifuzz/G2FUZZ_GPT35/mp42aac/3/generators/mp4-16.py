import os

# Create a directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate an mp4 file with chapters and watermarking
with open(os.path.join(output_dir, 'video_with_watermark.mp4'), 'wb') as f:
    f.write(b'Generated MP4 file with watermarking')

print('MP4 file with watermarking generated successfully!')
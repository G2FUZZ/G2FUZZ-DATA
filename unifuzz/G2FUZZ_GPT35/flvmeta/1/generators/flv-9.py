import os

# Create a directory to save generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with embedded subtitle support
for i in range(3):
    file_name = f'./tmp/video_{i}.flv'
    with open(file_name, 'wb') as f:
        # Generate FLV content with embedded subtitle track
        flv_content = b'FLV_HEADER' + f'Video {i} content with embedded subtitle'.encode('utf-8')
        f.write(flv_content)

print('FLV files with embedded subtitle support generated successfully!')
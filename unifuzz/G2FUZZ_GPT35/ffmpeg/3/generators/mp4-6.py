import os

# Create a directory to save generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with smaller file size
with open('./tmp/sample.mp4', 'wb') as f:
    # Write some sample data
    f.write(b'Sample mp4 file with compressed format leading to smaller file sizes')

print('Generated mp4 file with smaller file size successfully.')
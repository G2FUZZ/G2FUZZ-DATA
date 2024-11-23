import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create a dummy ICO file
def create_dummy_ico(path):
    # ICO header: 0 means 1 image, 1 is icon type, 1 is count, rest is image header
    ico_header = bytes([0, 0, 1, 0, 1, 0, 32, 32, 0, 0, 1, 0, 32, 0, 68, 16, 0, 0, 22, 0, 0, 0])
    with open(path, 'wb') as f:
        f.write(ico_header)
        # Write some dummy image data (this won't be a valid image)
        f.write(b'\x00' * 16 * 1024)  # Adjust size as needed

# Frame file paths
frame_paths = ['./tmp/frame1.ico', './tmp/frame2.ico']

# Create dummy ICO files if they don't exist
for frame_path in frame_paths:
    if not os.path.exists(frame_path):
        create_dummy_ico(frame_path)
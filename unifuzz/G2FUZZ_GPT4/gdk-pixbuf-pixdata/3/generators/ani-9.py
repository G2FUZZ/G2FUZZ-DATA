from PIL import Image, ImageDraw
import os

def create_ico_file(filepath, size=(32, 32), color=(255, 0, 0)):
    """
    Create a simple ICO file with specified size and color.
    """
    image = Image.new('RGBA', size, color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, size[0], size[1]), fill=color)
    image.save(filepath, format='ICO')

def create_ani_file(ani_filepath, ico_files, rate=60, seq=0):
    """
    Create an ANI file from a list of ICO filepaths.
    `rate` is the display rate of the frames in jiffies (1/60th of a second).
    `seq` is a sequence number for the ANI header.
    """
    # ANI header for RIFF format
    ani_header = (
        b'RIFF\x00\x00\x00\x00ACONanih\x24\x00\x00\x00\x24\x00\x00\x00'
        + rate.to_bytes(4, byteorder='little')  # Rate
        + seq.to_bytes(4, byteorder='little')  # Sequence
        + (len(ico_files) * 2).to_bytes(4, byteorder='little')  # Number of frames * 2 for sequence
        + b'\x00' * 16  # Padding
        + b'rate' + (len(ico_files) * 4).to_bytes(4, byteorder='little')  # RATE chunk
        + bytes([rate] * len(ico_files)) * 4  # Rate for each frame
        + b'seq ' + (len(ico_files) * 4).to_bytes(4, byteorder='little')  # SEQ chunk
        + bytes(range(len(ico_files))) * 4  # Sequence
    )

    # Calculate total size for RIFF
    total_size = 48 + (len(ico_files) * 8) + sum(os.path.getsize(f) for f in ico_files)  # Header + frame size
    ani_header = ani_header[:4] + total_size.to_bytes(4, byteorder='little') + ani_header[8:]

    # Open ANI file to write
    with open(ani_filepath, 'wb') as ani_file:
        ani_file.write(ani_header)  # Write the header

        # Write each frame
        for ico_file in ico_files:
            with open(ico_file, 'rb') as frame:
                ani_file.write(b'icon' + os.path.getsize(ico_file).to_bytes(4, byteorder='little'))
                ani_file.write(frame.read())

# Directory for temporary ICO and ANI files
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Create ICO files
ico_files = []
for i in range(3):  # Create 3 frames for demonstration
    ico_path = os.path.join(tmp_dir, f'frame_{i}.ico')
    create_ico_file(ico_path, size=(32, 32), color=(255, 0, 0))
    ico_files.append(ico_path)

# Create an ANI file
ani_filepath = os.path.join(tmp_dir, 'animated_cursor.ani')
create_ani_file(ani_filepath, ico_files)
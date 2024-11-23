from PIL import Image, ImageDraw
import os

def create_frame(color, size=(32, 32)):
    """Creates an individual frame for the .ani file."""
    image = Image.new("RGBA", size, color)
    draw = ImageDraw.Draw(image)
    # Example drawing: diagonal line
    draw.line((0, 0) + image.size, fill="black")
    draw.line((0, image.size[1], image.size[0], 0), fill="black")
    return image

def save_ani_file(filename, frames, durations):
    """Saves frames as an .ani file."""
    # ANI header structure and default values for a simple ANI file
    header = bytes("RIFF", 'ascii')  # RIFF header
    list_type = bytes("ACON", 'ascii')  # ACON - Animation Content
    ani_header = bytes("anih", 'ascii')  # ANI Header chunk
    seq_header = bytes("seq ", 'ascii')  # Sequence chunk
    frame_header = bytes("icon", 'ascii')  # Frame chunk

    # ANI Header specific fields
    header_size = 36  # ANI header size
    frames_count = len(frames)
    steps_count = frames_count
    width = frames[0].width
    height = frames[0].height
    bit_count = 32  # Assuming 32 bits for RGBA
    planes = 1
    jif_rate = int(60 / (1000 / durations[0]))  # Convert ms to jiffies (about 1/60th of a second)
    flags = 1  # Always 1

    # Create frames data
    frame_data = bytearray()
    for frame in frames:
        frame_bytes = frame.tobytes()
        frame_data += frame_header + len(frame_bytes).to_bytes(4, 'little') + frame_bytes

    # Create sequence data (simple sequence where each frame is used in order)
    seq_data = seq_header + (4 * frames_count).to_bytes(4, 'little') + bytearray(range(frames_count))

    # Calculate total size
    total_size = 4 + len(ani_header) + 4 + header_size + len(seq_data) + len(frame_data)

    with open(filename, "wb") as f:
        # Write RIFF header
        f.write(header)
        f.write(total_size.to_bytes(4, 'little'))
        f.write(list_type)

        # Write ANI header
        f.write(ani_header)
        f.write(header_size.to_bytes(4, 'little'))
        f.write(header_size.to_bytes(4, 'little'))
        f.write(frames_count.to_bytes(4, 'little'))
        f.write(steps_count.to_bytes(4, 'little'))
        f.write(width.to_bytes(4, 'little'))
        f.write(height.to_bytes(4, 'little'))
        f.write(bit_count.to_bytes(4, 'little'))
        f.write(planes.to_bytes(4, 'little'))
        f.write(jif_rate.to_bytes(4, 'little'))
        f.write(flags.to_bytes(4, 'little'))

        # Write sequence data
        f.write(seq_data)

        # Write frame data
        f.write(frame_data)

# Prepare frames
frames = [create_frame("red"), create_frame("blue")]
durations = [1000, 1000]  # Duration of each frame in milliseconds

# Ensure the tmp directory exists
os.makedirs("./tmp", exist_ok=True)

# Save the .ani file
save_ani_file("./tmp/animated_cursor.ani", frames, durations)

print("ANI file has been created.")
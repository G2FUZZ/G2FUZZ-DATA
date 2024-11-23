import os

def create_ani_file(file_path, ani_header, frames):
    with open(file_path, 'wb') as f:
        f.write(ani_header)
        for frame in frames:
            f.write(frame)

def generate_ani_header(rate=60):
    # ANI Header Structure for a basic animation with customizable speed
    # RIFF header
    riff = b'RIFF'
    list_ = b'LIST'
    # Calculating size placeholder for now
    riff_size = b'    '
    acnl = b'ACON'
    # ANI Header
    anih = b'anih'
    anih_size = (36).to_bytes(4, byteorder='little') # Size of the ANIH header
    frames = (2).to_bytes(4, byteorder='little') # Number of frames
    steps = (2).to_bytes(4, byteorder='little') # Number of steps (usually same as frames)
    width = (32).to_bytes(4, byteorder='little') # Width of frame (icon)
    height = (32).to_bytes(4, byteorder='little') # Height of frame (icon)
    bit_count = (8).to_bytes(4, byteorder='little') # Bits per pixel
    planes = (1).to_bytes(4, byteorder='little') # Number of color planes
    jifRate = (rate).to_bytes(4, byteorder='little') # Frame display rate (jiffies)
    flags = (1).to_bytes(4, byteorder='little') # Flags (1 = Animated cursor)
    
    # Calculating the overall size of the ANI file (simplified for this example)
    overall_size = 36 + 8 # Simplified size calculation
    riff_size = overall_size.to_bytes(4, byteorder='little')
    
    ani_header = riff + riff_size + acnl + list_ + riff_size + anih + anih_size + frames + steps + width + height + bit_count + planes + jifRate + flags
    return ani_header

def generate_frame_data():
    # Placeholder function to generate frame data (ICONDIRENTRY + icon data)
    # For simplicity, this will be static data representing two 32x32 pixel frames
    frame_data = []
    frame_data.append(b'\x00' * 256) # Frame 1 (purely an example, not actual icon data)
    frame_data.append(b'\xFF' * 256) # Frame 2 (purely an example, not actual icon data)
    return frame_data

# Example usage
ani_header = generate_ani_header(rate=60) # 60 jiffies (1 second per frame)
frames = generate_frame_data()
file_path = './tmp/custom_animation.ani'
os.makedirs(os.path.dirname(file_path), exist_ok=True)
create_ani_file(file_path, ani_header, frames)

print(f"ANI file created at {file_path}")
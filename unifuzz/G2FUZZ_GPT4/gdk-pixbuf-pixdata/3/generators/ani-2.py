from PIL import Image
import os

def create_frames(num_frames=10):
    frames = []
    for i in range(num_frames):
        img = Image.new('RGBA', (32, 32), (i*25 % 255, 255 - i*25 % 255, i*10 % 255))
        frames.append(img)
    return frames

def save_ani_file(frames, file_path='./tmp/animated_cursor.ani'):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'wb') as f:
        # ANI header structure
        f.write(b'RIFF')  # ChunkID
        # Corrected ChunkSize calculation by removing frame.n_frames and assuming each frame is a single image
        f.write((36 + (len(frames) * 4) + (len(frames) * 36) + sum(1 * frame.size[0] * frame.size[1] * 4 for frame in frames)).to_bytes(4, byteorder='little'))  # ChunkSize
        f.write(b'ACON')  # FormType

        # ANI header
        f.write(b'anih')  # ChunkID
        f.write((36).to_bytes(4, byteorder='little'))  # ChunkSize
        f.write((36).to_bytes(4, byteorder='little'))  # cbSizeOf
        f.write(len(frames).to_bytes(4, byteorder='little'))  # cFrames
        f.write(len(frames).to_bytes(4, byteorder='little'))  # cSteps
        f.write((0).to_bytes(4, byteorder='little'))  # cx, cy (reserved, must be 0)
        f.write((0).to_bytes(4, byteorder='little'))  # cBitCount, cPlanes (reserved, must be 0)
        f.write((0).to_bytes(4, byteorder='little'))  # JifRate
        f.write((0).to_bytes(4, byteorder='little'))  # flags

        # Sequence
        f.write(b'seq ')  # ChunkID
        f.write((4 + len(frames) * 4).to_bytes(4, byteorder='little'))  # ChunkSize
        f.write(len(frames).to_bytes(4, byteorder='little'))  # cbSizeOf
        for i in range(len(frames)):
            f.write(i.to_bytes(4, byteorder='little'))  # Step

        # Writing frames
        for i, frame in enumerate(frames):
            frame_data = frame.tobytes()
            f.write(b'fram')  # ChunkID
            # ChunkSize: 4 bytes (biSize) + 40 bytes (BITMAPINFOHEADER) + len(frame_data)
            f.write((4 + 40 + len(frame_data)).to_bytes(4, byteorder='little'))
            f.write(b'ico ')  # ChunkType
            f.write((40 + len(frame_data)).to_bytes(4, byteorder='little'))  # biSizeImage (size of the bitmap data)
            f.write((frame.size[0]).to_bytes(4, byteorder='little'))  # biWidth
            f.write((frame.size[1] * 2).to_bytes(4, byteorder='little'))  # biHeight
            f.write((1).to_bytes(2, byteorder='little'))  # biPlanes
            f.write((32).to_bytes(2, byteorder='little'))  # biBitCount
            f.write((0).to_bytes(4, byteorder='little'))  # biCompression
            f.write(len(frame_data).to_bytes(4, byteorder='little'))  # biSizeImage
            f.write((0).to_bytes(4, byteorder='little'))  # biXPelsPerMeter
            f.write((0).to_bytes(4, byteorder='little'))  # biYPelsPerMeter
            f.write((0).to_bytes(4, byteorder='little'))  # biClrUsed
            f.write((0).to_bytes(4, byteorder='little'))  # biClrImportant
            f.write(frame_data)  # Image data

frames = create_frames(10)
save_ani_file(frames)
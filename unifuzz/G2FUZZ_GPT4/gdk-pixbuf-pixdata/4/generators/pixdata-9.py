import os
import struct
import numpy as np

def create_pixdata_file(filename, frames, durations):
    """
    Create a .pixdata file with animation support.

    :param filename: The path to the file to be created.
    :param frames: A list of numpy arrays representing the frames.
    :param durations: A list of integers representing the duration of each frame in milliseconds.
    """
    # Ensure the tmp directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'wb') as f:
        # Write the number of frames
        f.write(struct.pack('I', len(frames)))
        
        for duration, frame in zip(durations, frames):
            # Write the frame duration
            f.write(struct.pack('I', duration))
            
            # Flatten the frame data and write it
            flattened_frame = frame.flatten()
            frame_data = struct.pack(f'{len(flattened_frame)}B', *flattened_frame)
            f.write(frame_data)

# Example usage
if __name__ == "__main__":
    # Generate some dummy frames (10x10 pixels, 3 channels RGB)
    num_frames = 4
    frames = [np.random.randint(0, 256, (10, 10, 3), dtype=np.uint8) for _ in range(num_frames)]
    durations = [100, 200, 300, 400]  # Durations in milliseconds
    
    create_pixdata_file('./tmp/animation.pixdata', frames, durations)
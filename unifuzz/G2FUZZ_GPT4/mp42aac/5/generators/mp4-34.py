import cv2
import numpy as np
import os

def create_background(frame_number, height, width):
    """
    Create a dynamic background based on the frame number.
    This example creates a gradient that moves.
    """
    background = np.zeros((height, width, 3), dtype=np.uint8)
    x = int((frame_number % width) * 1.5) % width  # Moving x for gradient
    for i in range(height):
        cv2.line(background, (x, i), (width//2, i), (255 - i % 255, i % 255, (i + x) % 255), 1)
    return background

def add_animated_shapes(frame, frame_number):
    """
    Add animated shapes that change position with the frame number.
    """
    # Circle
    cv2.circle(frame, (frame_number % 500, 200), 50, (0, 0, 255), -1)
    # Rectangle that moves
    cv2.rectangle(frame, (400, frame_number % 480), (500, (frame_number % 480) + 100), (0, 255, 0), -1)

def add_dynamic_text(frame, frame_number):
    """
    Add dynamic text that changes its properties with the frame number.
    """
    font_scale = 1 + (np.sin(frame_number / 20) * 1)
    cv2.putText(frame, f'Frame {frame_number+1}', (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 
                font_scale, (255, 255, 255), 2)

def main():
    # Ensure the output directory exists
    output_dir = './tmp/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Video properties
    width, height = 640, 480
    fps = 24
    duration = 5  # seconds
    video_file_path = os.path.join(output_dir, 'complex_output.mp4')

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MPEG-4 codec
    out = cv2.VideoWriter(video_file_path, fourcc, fps, (width, height))

    # Generate frames with more complex structures
    for i in range(fps * duration):
        # Create a dynamic background
        frame = create_background(i, height, width)
        # Add animated shapes
        add_animated_shapes(frame, i)
        # Add dynamic text
        add_dynamic_text(frame, i)
        # Write the frame into the file
        out.write(frame)

    # Release everything when the job is finished
    out.release()
    print(f'Video saved to {video_file_path}')

if __name__ == "__main__":
    main()
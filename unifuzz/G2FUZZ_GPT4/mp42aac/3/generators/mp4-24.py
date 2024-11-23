import cv2
import numpy as np
import os

def generate_video(output_path, resolution, text_scale, ellipse_scale):
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Changed to 'mp4v' for broader compatibility
    out = cv2.VideoWriter(output_path, fourcc, 20.0, resolution)

    # Generate 100 frames with dynamic content
    for i in range(100):
        # Create a blank image with some dynamic elements
        img = np.zeros((resolution[1], resolution[0], 3), np.uint8)
        cv2.putText(img, f'Frame {i}', (50, int(230 * ellipse_scale)), cv2.FONT_HERSHEY_SIMPLEX, 
                    text_scale, (255, 255, 255), int(3 * ellipse_scale), cv2.LINE_AA)
        cv2.ellipse(img, (int(320 * ellipse_scale), int(240 * ellipse_scale)), 
                    (int(100 * ellipse_scale), int(50 * ellipse_scale)), 0, 0, i*360/100, 
                    (255, 0, 0), -1)

        # Write the frame into the file
        out.write(img)

    # Release everything when the job is finished
    out.release()

# High-resolution video
high_res_output_path = './tmp/output_high_res.mp4'
generate_video(high_res_output_path, (640, 480), 2, 1)

# Low-resolution (alternate track) video
low_res_output_path = './tmp/output_low_res.mp4'
generate_video(low_res_output_path, (320, 240), 1, 0.5)  # Corrected the variable name here

print(f"High-resolution video successfully saved to {high_res_output_path}")
print(f"Low-resolution video (alternate track) successfully saved to {low_res_output_path}")

# Note: To actually combine these into a single MP4 file with alternate tracks, additional steps are required
# using a tool like FFmpeg. This example solely demonstrates the creation of two separate tracks.
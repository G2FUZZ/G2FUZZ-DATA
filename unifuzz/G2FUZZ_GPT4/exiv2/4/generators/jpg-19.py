import numpy as np
import cv2
import os

# Apply DCT to each channel
def apply_dct(channel):
    # Convert to float32 for DCT
    channel_float = channel.astype(np.float32)
    # Apply DCT
    dct = cv2.dct(channel_float)
    # Quantization - simple way by dividing by a constant and rounding
    dct_quanted = np.round(dct / 16)
    # Inverse DCT to get back to spatial domain
    channel_recovered = cv2.idct(dct_quanted)
    # Clip values and convert back to uint8
    channel_recovered = np.clip(channel_recovered, 0, 255).astype(np.uint8)
    return channel_recovered

def generate_dct_image(width, height, filename):
    # Create a directory if it does not exist
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    
    # Generate a random image
    img = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    # Convert image to YCrCb color space
    img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    
    # Split the channels
    y, cr, cb = cv2.split(img_ycrcb)
    
    # Apply DCT compression simulation and inverse for each channel
    y_dct = apply_dct(y)
    cr_dct = apply_dct(cr)
    cb_dct = apply_dct(cb)
    
    # Merge the channels back
    img_dct = cv2.merge([y_dct, cr_dct, cb_dct])
    
    # Convert back to BGR color space for saving
    img_dct_bgr = cv2.cvtColor(img_dct, cv2.COLOR_YCrCb2BGR)
    
    # Save the image
    cv2.imwrite(f'./tmp/{filename}', img_dct_bgr)

def generate_mjpeg_video(width, height, video_filename, num_frames=10):
    # Create a directory if it does not exist
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(f'./tmp/{video_filename}', fourcc, 20.0, (width, height))
    
    for _ in range(num_frames):
        # Generate a random image
        img = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
        
        # Convert image to YCrCb color space
        img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        
        # Split the channels
        y, cr, cb = cv2.split(img_ycrcb)
        
        # Apply DCT to each channel and merge back
        img_dct = cv2.merge([apply_dct(y), apply_dct(cr), apply_dct(cb)])
        
        # Convert back to BGR for video
        img_dct_bgr = cv2.cvtColor(img_dct, cv2.COLOR_YCrCb2BGR)
        
        # Write the frame
        out.write(img_dct_bgr)
    
    # Release everything if job is finished
    out.release()

# Example usage
generate_dct_image(256, 256, 'dct_compressed.jpg')
generate_mjpeg_video(256, 256, 'mjpeg_video.avi', num_frames=30)
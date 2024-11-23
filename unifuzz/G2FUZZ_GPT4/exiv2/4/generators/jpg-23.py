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

def generate_dct_image_12bit(width, height, filename):
    # Create a directory if it does not exist
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    
    # Generate a random image with 12-bit depth
    img = np.random.randint(0, 4096, (height, width, 3), dtype=np.uint16)
    
    # Convert image to YCrCb color space
    img_ycrcb = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_BGR2YCrCb)
    
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
    
    # Scale the 8-bit image back to 12-bit for demonstration purposes
    # Normally, JPEG doesn't support 12-bit, but for simulation, we upscale the values
    img_dct_bgr_12bit = np.clip(img_dct_bgr.astype(np.uint16) * 16, 0, 4095)
    
    # Save the image - NOTE: This will still save as an 8-bit image since OpenCV does not support saving in 12-bit JPEG
    # This step is purely for demonstration, assuming further processing for 12-bit support
    cv2.imwrite(f'./tmp/{filename}', img_dct_bgr_12bit.astype(np.uint8))

# Example usage
generate_dct_image_12bit(256, 256, 'dct_compressed_12bit.jpg')
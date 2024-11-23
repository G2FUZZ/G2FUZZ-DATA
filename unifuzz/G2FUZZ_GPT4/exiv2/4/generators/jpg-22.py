import numpy as np
import cv2
import os

def generate_dct_image_with_color_profile(width, height, filename, color_profile='sRGB'):
    # Create a directory if it does not exist
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    
    # Generate a random image
    img = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    # Convert image to YCrCb color space
    img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    
    # Split the channels
    y, cr, cb = cv2.split(img_ycrcb)
    
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
    
    # Apply DCT compression simulation and inverse for each channel
    y_dct = apply_dct(y)
    cr_dct = apply_dct(cr)
    cb_dct = apply_dct(cb)
    
    # Merge the channels back
    img_dct = cv2.merge([y_dct, cr_dct, cb_dct])
    
    # Convert back to BGR color space for saving
    img_dct_bgr = cv2.cvtColor(img_dct, cv2.COLOR_YCrCb2BGR)
    
    # Depending on the color profile, convert the color space accordingly
    if color_profile == 'Adobe RGB':
        # Simulating conversion to Adobe RGB by applying a transformation matrix. 
        # In a real scenario, this should be replaced by proper color management practices.
        # Adobe RGB is assumed to be simulated here for educational purposes.
        img_dct_bgr = (img_dct_bgr.astype(np.float32) / 255.0) ** (2.2/1.8) * 255.0  # Simplified gamma correction
        img_dct_bgr = np.clip(img_dct_bgr, 0, 255).astype(np.uint8)

    # Save the image
    # Note: OpenCV does not directly support embedding ICC profiles like sRGB or Adobe RGB in JPEG files.
    # The color transformation applied above is a simplification and may not accurately represent the color profiles.
    cv2.imwrite(f'./tmp/{filename}', img_dct_bgr)

# Example usage
generate_dct_image_with_color_profile(256, 256, 'dct_compressed_sRGB.jpg', 'sRGB')
generate_dct_image_with_color_profile(256, 256, 'dct_compressed_AdobeRGB.jpg', 'Adobe RGB')
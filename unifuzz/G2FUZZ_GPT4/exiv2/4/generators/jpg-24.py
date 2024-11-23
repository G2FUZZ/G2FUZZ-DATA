import numpy as np
import cv2
import os
from PIL import Image, ExifTags

def generate_dct_image_with_color_profile_and_mpf(width, height, filename, color_profile='sRGB'):
    # Create a directory if it does not exist
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    
    # Generate two random images, one as the original and one as the modified version
    img1 = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    img2 = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    # Convert images to YCrCb color space and apply DCT compression simulation and inverse
    def process_image(img):
        img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        y, cr, cb = cv2.split(img_ycrcb)
        def apply_dct(channel):
            channel_float = channel.astype(np.float32)
            dct = cv2.dct(channel_float)
            dct_quanted = np.round(dct / 16)
            channel_recovered = cv2.idct(dct_quanted)
            channel_recovered = np.clip(channel_recovered, 0, 255).astype(np.uint8)
            return channel_recovered
        y_dct = apply_dct(y)
        cr_dct = apply_dct(cr)
        cb_dct = apply_dct(cb)
        img_dct = cv2.merge([y_dct, cr_dct, cb_dct])
        img_dct_bgr = cv2.cvtColor(img_dct, cv2.COLOR_YCrCb2BGR)
        if color_profile == 'Adobe RGB':
            img_dct_bgr = (img_dct_brg.astype(np.float32) / 255.0) ** (2.2/1.8) * 255.0
            img_dct_bgr = np.clip(img_dct_bgr, 0, 255).astype(np.uint8)
        return img_dct_bgr
    
    img1_processed = process_image(img1)
    img2_processed = process_image(img2)
    
    # Save the processed images temporarily
    cv2.imwrite(f'./tmp/temp1.jpg', img1_processed)
    cv2.imwrite(f'./tmp/temp2.jpg', img2_processed)
    
    # Use PIL to combine the images into a single file with Multi-Picture Format (MPF) information
    img1_pil = Image.open(f'./tmp/temp1.jpg')
    img2_pil = Image.open(f'./tmp/temp2.jpg')
    
    # Assuming both images have the same dimensions and mode
    img1_pil.info['mpf'] = bytes('MPF: Multi-Picture Format', 'utf-8')
    
    # Save the MPF image in TIFF format
    mpf_filename = f'./tmp/{filename}.tiff'  # Ensure the filename ends with .tiff
    img1_pil.save(mpf_filename, format='TIFF', save_all=True, append_images=[img2_pil])

    # Cleanup temporary files
    os.remove(f'./tmp/temp1.jpg')
    os.remove(f'./tmp/temp2.jpg')

# Example usage
generate_dct_image_with_color_profile_and_mpf(256, 256, 'dct_compressed_MPF', 'sRGB')
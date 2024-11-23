import numpy as np
import cv2
import os
from scipy.fftpack import dct, idct
from PIL import Image, ImageDraw, ImageFont, ImageCms
import piexif
from lxml import etree as ET

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_complex_image(quality=90, embed_text=True, text="Complex JPEG"):
    # Generate a random 512x512 RGB image
    img = np.random.randint(0, 256, (512, 512, 3), dtype=np.uint8)

    # Function to apply DCT and IDCT
    def dct2(a):
        return dct(dct(a, axis=0, norm='ortho'), axis=1, norm='ortho')

    def idct2(a):
        return idct(idct(a, axis=0, norm='ortho'), axis=1, norm='ortho')

    # Applying DCT on blocks of 8x8 for each channel
    img_dct = np.zeros_like(img, dtype=float)
    for k in range(3):  # For each color channel
        for i in np.r_[:img.shape[0]:8]:
            for j in np.r_[:img.shape[1]:8]:
                img_dct[i:(i+8), j:(j+8), k] = dct2(img[i:(i+8), j:(j+8), k])

    # Inverse DCT
    img_idct = np.zeros_like(img, dtype=float)
    for k in range(3):  # For each color channel
        for i in np.r_[:img_dct.shape[0]:8]:
            for j in np.r_[:img_dct.shape[1]:8]:
                img_idct[i:(i+8), j:(j+8), k] = idct2(img_dct[i:(i+8), j:(j+8), k])

    # Convert back to uint8
    img_idct = np.clip(img_idct, 0, 255).astype(np.uint8)

    # Create a PIL Image for further processing
    img_pil = Image.fromarray(img_idct)

    # Generate multiple layers with varying transparencies
    for i in range(3):
        overlay = Image.new('RGB', (100, 100), color=(255-i*40, 100+i*50, 150-i*25))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.text((10, 10), f"Layer {i+1}", fill=(255, 255, 255))
        
        # Create a mask with the same dimensions as the overlay and fill it with white (full opacity)
        mask = Image.new('L', (100, 100), color=255)
        
        # Use the mask when pasting
        img_pil.paste(overlay, (i*100, i*100), mask)

    # Add multiple textual watermarks in different orientations
    draw = ImageDraw.Draw(img_pil)
    watermark_texts = ["Watermark 1", "Watermark 2", "Watermark 3"]
    for i, watermark_text in enumerate(watermark_texts):
        try:
            font = ImageFont.truetype("arial.ttf", 24)  # Ensure the font path and size is correctly set
        except IOError:
            font = ImageFont.load_default()
        draw.text((10, img_pil.height - 150 + i*50), watermark_text, (255, i*80, i*80), font=font)

    # Convert back to OpenCV format
    img_final = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    # Save the intermediate result
    intermediate_filename = f'./tmp/complex_intermediate_{quality}.jpg'
    cv2.imwrite(intermediate_filename, img_final, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

    # Embedding ICC profile, EXIF, and XMP metadata should be done here as previously described

    # Note: Ensure the embedding ICC profile, EXIF, and XMP metadata code is correctly implemented here

    print(f"Complex image with advanced features and complex file structures saved to {intermediate_filename}")

generate_complex_image()
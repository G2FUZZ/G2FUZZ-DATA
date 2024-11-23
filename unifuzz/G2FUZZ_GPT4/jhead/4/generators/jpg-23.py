import numpy as np
import cv2
import os
from scipy.fftpack import dct, idct
from PIL import Image, PngImagePlugin

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_image_with_advanced_features(quality=90, embed_text=True, text="Advanced JPEG"):
    # Generate a random 256x256 RGB image
    img = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)

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

    # Save the result with specified quality
    filename = f'./tmp/advanced_features_demo_{quality}.jpg'
    cv2.imwrite(filename, cv2.cvtColor(img_idct, cv2.COLOR_RGB2BGR), [int(cv2.IMWRITE_JPEG_QUALITY), quality])

    # Embed textual metadata if required
    if embed_text:
        image = Image.open(filename)
        meta = PngImagePlugin.PngInfo()
        meta.add_text("Description", text)
        image.save(filename, "JPEG", quality=quality, pnginfo=meta)

    print(f"Image with advanced features saved to {filename}")

generate_image_with_advanced_features()
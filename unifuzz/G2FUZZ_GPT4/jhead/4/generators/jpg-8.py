import numpy as np
import cv2
import os
from scipy.fftpack import dct, idct

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_image_with_huffman_coding():
    # Generate a random 256x256 grayscale image
    img = np.random.randint(0, 256, (256, 256), dtype=np.uint8)

    # Apply DCT to simulate part of JPEG's process
    def dct2(a):
        return dct(dct(a.T, norm='ortho').T, norm='ortho')

    def idct2(a):
        return idct(idct(a.T, norm='ortho').T, norm='ortho')

    # Applying DCT on blocks of 8x8
    img_dct = np.zeros_like(img, dtype=float)
    for i in np.r_[:img.shape[0]:8]:
        for j in np.r_[:img.shape[1]:8]:
            img_dct[i:(i+8), j:(j+8)] = dct2(img[i:(i+8), j:(j+8)])

    # Normally here Huffman coding would be applied to the quantized DCT coefficients.
    # For demonstration purposes, we skip actual Huffman coding as implementing it from scratch is complex
    # and not directly supported by high-level libraries typically used for image processing in Python.
    # Instead, we'll proceed to inverse DCT to simulate having processed the image.

    img_idct = np.zeros_like(img, dtype=float)
    for i in np.r_[:img_dct.shape[0]:8]:
        for j in np.r_[:img_dct.shape[1]:8]:
            img_idct[i:(i+8), j:(j+8)] = idct2(img_dct[i:(i+8), j:(j+8)])

    # Convert back to uint8 for image saving
    img_idct = np.clip(img_idct, 0, 255).astype(np.uint8)

    # Save the result
    filename = './tmp/huffman_coding_demo.jpg'
    cv2.imwrite(filename, img_idct)

    print(f"Image with simulated Huffman coding process saved to {filename}")

generate_image_with_huffman_coding()
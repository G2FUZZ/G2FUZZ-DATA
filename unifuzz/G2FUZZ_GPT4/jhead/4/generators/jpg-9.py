import numpy as np
import os
from scipy.fftpack import dct, idct
from PIL import Image

def create_gradient_image(width, height):
    """Create a simple gradient image."""
    x = np.linspace(0, 1, width)
    y = np.linspace(0, 1, height)
    X, Y = np.meshgrid(x, y)
    Z = (X + Y) / 2 * 255
    return Z.astype(np.uint8)

def apply_dct(image):
    """Apply 2D Discrete Cosine Transform."""
    return dct(dct(image, axis=0, norm='ortho'), axis=1, norm='ortho')

def apply_idct(transformed):
    """Apply 2D Inverse Discrete Cosine Transform."""
    return idct(idct(transformed, axis=0, norm='ortho'), axis=1, norm='ortho')

def quantize_dct(dct_matrix, quantization_matrix):
    """Quantize DCT based on a quantization matrix."""
    return (dct_matrix / quantization_matrix).round() * quantization_matrix

def simulate_jpeg_compression(image, quantization_matrix):
    """Simulate JPEG compression by applying and inversing DCT."""
    dct_applied = apply_dct(image)
    quantized = quantize_dct(dct_applied, quantization_matrix)
    recovered_image = apply_idct(quantized)
    return np.clip(recovered_image, 0, 255).astype(np.uint8)

# Create a simple gradient image
width, height = 256, 256
gradient_image = create_gradient_image(width, height)

# Define a simple quantization matrix for demonstration purposes
quantization_matrix = np.full((width, height), 50)

# Simulate JPEG compression
jpeg_simulated_image = simulate_jpeg_compression(gradient_image.astype(float), quantization_matrix)

# Save the image
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_path = os.path.join(output_dir, 'jpeg_compressed.jpg')
Image.fromarray(jpeg_simulated_image).save(output_path)

print(f"JPEG simulated image saved to {output_path}")
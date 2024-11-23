import numpy as np
import matplotlib.pyplot as plt
import os
import qrcode  # For generating QR code which includes error correction capability

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an image with varying brightness
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)

# Create a gradient from left (black) to right (white)
# For sRGB, we use a 3-channel image
for x in range(width):
    color_value = x
    image[:, x, :] = [color_value, color_value, color_value]  # RGB

# Apply gamma correction for sRGB
def srgb_gamma_correction(channel):
    # Normalize the pixel values
    channel = channel / 255.0
    # Apply sRGB gamma correction
    channel = np.where(channel <= 0.0031308,
                       channel * 12.92,
                       1.055 * np.power(channel, 1/2.4) - 0.055)
    return np.array(channel * 255, dtype='uint8')

image_srgb_gamma_corrected = np.zeros_like(image)
for i in range(3):  # Apply the correction to each channel
    image_srgb_gamma_corrected[:, :, i] = srgb_gamma_correction(image[:, :, i])

# Save the original and sRGB gamma-corrected images
plt.imsave(f'{output_dir}original_rgb.png', image)
plt.imsave(f'{output_dir}srgb_gamma_corrected.png', image_srgb_gamma_corrected)

# Generating a QR code with error correction capability for data integrity
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)
qr.add_data('Error Correction Codes feature included')
qr.make(fit=True)

# Convert QR code to an image
img_qr = qr.make_image(fill_color="black", back_color="white")
qr_code_path = f'{output_dir}error_correction_codes_qr.png'
img_qr.save(qr_code_path)

print(f"Original and sRGB gamma-corrected images saved in {output_dir}")
print(f"QR code with Error Correction Codes feature saved as {qr_code_path}")
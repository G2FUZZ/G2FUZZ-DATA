import numpy as np
import cv2
import os
from scipy.fftpack import dct, idct
from PIL import Image, ImageDraw, ImageFont, ExifTags, PngImagePlugin, ImageCms
import piexif

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

    # Create a PIL Image for further processing
    img_pil = Image.fromarray(img_idct)

    # Composite Image: Instead of loading an image, generate a small placeholder image
    small_img = Image.new('RGB', (64, 64), color = (73, 109, 137))
    img_pil.paste(small_img, (10, 10))  # Pasting at position (10, 10)

    # Add a watermark
    draw = ImageDraw.Draw(img_pil)
    watermark_text = "Watermark"
    try:
        font = ImageFont.truetype("arial.ttf", 36)  # Ensure the font path and size is correctly set
    except IOError:
        # Fallback if the specified font is not found
        font = ImageFont.load_default()  # Corrected from Image0Font to ImageFont
    draw.text((10, img_pil.height - 50), watermark_text, (255, 255, 255), font=font)

    # Convert back to OpenCV format
    img_final = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    # Save the intermediate result to adjust EXIF later
    intermediate_filename = f'./tmp/intermediate_{quality}.jpg'
    cv2.imwrite(intermediate_filename, img_final, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

    # Embedding ICC profile
    sRGB_profile = ImageCms.createProfile("sRGB")
    img_pil = ImageCms.profileToProfile(img_pil, sRGB_profile, sRGB_profile, outputMode='RGB')

    # Embed textual metadata and EXIF data if required
    if embed_text:
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}}
        exif_dict["0th"][piexif.ImageIFD.Make] = "Advanced JPEG Generator"
        exif_dict["0th"][piexif.ImageIFD.XResolution] = (300, 1)
        exif_dict["0th"][piexif.ImageIFD.YResolution] = (300, 1)
        exif_dict["0th"][piexif.ImageIFD.Software] = "Custom Python Script"
        
        # Embedding GPS Information
        exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = 'N'
        exif_dict["GPS"][piexif.GPSIFD.GPSLatitude] = [(37, 1), (52, 1), (23, 1)]
        exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef] = 'W'
        exif_dict["GPS"][piexif.GPSIFD.GPSLongitude] = [(122, 1), (30, 1), (0, 1)]
        
        exif_bytes = piexif.dump(exif_dict)

        # Save final image with embedded ICC profile and EXIF data
        final_filename = f'./tmp/advanced_features_demo_{quality}.jpg'
        img_pil.save(final_filename, "JPEG", quality=quality, exif=exif_bytes)

    print(f"Image with advanced features and complex file structures saved to {final_filename}")

generate_image_with_advanced_features()
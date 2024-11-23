import numpy as np
import cv2
import os
from scipy.fftpack import dct, idct
from PIL import Image, ImageDraw, ImageFont, ExifTags, PngImagePlugin, ImageCms
import piexif

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def generate_complex_image(quality=90, embed_text=True, text="Complex JPEG", watermark_text="Complex Watermark"):
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

    # Add custom-shaped cropping (e.g., circle)
    mask = Image.new('L', img_pil.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((50, 50, 450, 450), fill=255)
    img_pil.putalpha(mask)
    img_pil = img_pil.crop((50, 50, 450, 450))

    # Add multi-layered watermarks
    draw = ImageDraw.Draw(img_pil)
    try:
        font = ImageFont.truetype("arial.ttf", 24)  # Ensure the font path and size is correctly set
    except IOError:
        font = ImageFont.load_default()

    for i in range(0, img_pil.width, 100):
        for j in range(0, img_pil.height, 50):
            draw.text((i, j), watermark_text, (255, 255, 255, 128), font=font)  # Semi-transparent watermark

    # Ensure the image is in RGB (this step replaces the profileToProfile conversion)
    img_pil = img_pil.convert("RGB")

    # Convert back to OpenCV format
    img_final = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    # Save the intermediate result to adjust EXIF later, without alpha since JPEG does not support alpha
    intermediate_filename = f'./tmp/complex_intermediate_{quality}.jpg'
    cv2.imwrite(intermediate_filename, img_final, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

    # Embed textual metadata and EXIF data if required
    if embed_text:
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}}
        exif_dict["0th"][piexif.ImageIFD.Make] = "Complex JPEG Generator"
        exif_dict["0th"][piexif.ImageIFD.XResolution] = (300, 1)
        exif_dict["0th"][piexif.ImageIFD.YResolution] = (300, 1)
        exif_dict["0th"][piexif.ImageIFD.Software] = "Advanced Python Script"
        
        # Complex EXIF data, such as custom lens information
        exif_dict["Exif"][piexif.ExifIFD.LensMake] = "MyLens"
        exif_dict["Exif"][piexif.ExifIFD.LensSpecification] = [(35, 1), (70, 1), (28, 10), (28, 10)]
        
        exif_bytes = piexif.dump(exif_dict)

        # Save final image with embedded EXIF data
        final_filename = f'./tmp/complex_features_demo_{quality}.jpg'
        img_pil.save(final_filename, "JPEG", quality=quality, exif=exif_bytes)

    print(f"Complex image with advanced features and multi-layered watermarks saved to {final_filename}")

generate_complex_image()
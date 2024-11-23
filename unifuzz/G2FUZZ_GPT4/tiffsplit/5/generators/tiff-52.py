from PIL import Image, TiffImagePlugin, ImageDraw, ImageFont
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create images with varying properties and additional metadata
def create_image(size, color, text, dpi, color_space="RGB", metadata=None):
    if color_space == "L":  # Grayscale
        image = Image.new("L", size, color=1)  # 1 for white in grayscale
    else:  # Default to RGB
        image = Image.new("RGB", size, color=color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # Using default font
    draw.text((10, 10), text, fill="black" if color_space == "RGB" else 255, font=font)
    image.info['dpi'] = dpi
    if metadata:
        for key, value in metadata.items():
            image.info[key] = value
    return image

# Create multiple images with varying properties and metadata
image1 = create_image((100, 100), (255, 0, 0), "Page 1", (72, 72), metadata={"Title": "Red Square", "Author": "Artist 1"})
image2 = create_image((150, 150), 0, "Page 2", (300, 300), color_space="L", metadata={"Title": "Gray Square", "Author": "Artist 2"})
image3 = create_image((200, 100), (0, 0, 255), "Page 3", (96, 96), metadata={"Title": "Blue Rectangle", "Author": "Artist 3"})

# Function to save images as a multi-page TIFF with custom tags
def save_tiff_with_tags(path, images):
    # Configure first image
    first_image, *other_images = images
    first_image.save(
        path,
        save_all=True,
        compression="tiff_lzw",
        append_images=other_images,
        dpi=first_image.info['dpi'],
        tiffinfo={
            315: first_image.info.get('Author', ''),
            270: first_image.info.get('Title', '')
        }
    )

    # Save additional images with their specific DPI and metadata
    for img in other_images:
        with TiffImagePlugin.AppendingTiffWriter(path, True) as tf:
            img.save(
                tf,
                dpi=img.info['dpi'],
                tiffinfo={
                    315: img.info.get('Author', ''),
                    270: img.info.get('Title', '')
                }
            )

tiff_path = './tmp/multi_feature_tiff_with_complex_structure.tiff'
save_tiff_with_tags(tiff_path, [image1, image2, image3])

print(f"Generated TIFF with complex file structures at {tiff_path}")
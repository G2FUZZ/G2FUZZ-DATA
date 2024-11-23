import numpy as np
from PIL import Image, ImageDraw
import tifffile
from PIL import ImageCms

def generate_halftone_pattern(width, height, pattern_density):
    """Generates a simple halftone pattern for demonstration."""
    image = np.zeros((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            intensity = (x + y) % width
            if intensity < width // 3:
                if (x % (3 + pattern_density) == 0 and y % (3 + pattern_density) == 0):
                    image[y, x] = 0
                else:
                    image[y, x] = 255
            elif intensity < 2 * (width // 3):
                if (x % (4 + pattern_density) == 0 and y % (4 + pattern_density) == 0) or (x % (4 + pattern_density) == 2 and y % (4 + pattern_density) == 2):
                    image[y, x] = 0
                else:
                    image[y, x] = 255
            else:
                if (x % (5 + pattern_density) == 0 and y % (5 + pattern_density) == 0):
                    image[y, x] = 0
                else:
                    image[y, x] = 255
    return image

def add_text_to_image(image, text, position=(10, 10), color='white'):
    """Adds text to an image."""
    image_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(image_pil)
    draw.text(position, text, fill=color)
    return np.array(image_pil)

def generate_thumbnail(image, thumbnail_size=(50, 50)):
    """Generates a thumbnail of the given image."""
    image_pil = Image.fromarray(image)
    image_pil.thumbnail(thumbnail_size)
    return np.array(image_pil)

def save_with_subifds_and_metadata(images, file_path, descriptions):
    """Saves a list of numpy arrays as a multi-page TIFF file with subdirectories for thumbnails and additional metadata."""
    with tifffile.TiffWriter(file_path, bigtiff=True) as tiff:
        for i, img in enumerate(images):
            # Embed ICC profile
            icc_profile = ImageCms.createProfile("sRGB")
            img_pil = Image.fromarray(img).convert("RGB")
            img_with_icc = ImageCms.profileToProfile(img_pil, icc_profile, icc_profile, outputMode='RGB')
            
            # Add text to each image
            img_with_text = add_text_to_image(np.array(img_with_icc), f"Pattern {i+1}")
            thumbnail = generate_thumbnail(img_with_text)
            subifds = [{'shape': thumbnail.shape, 'dtype': thumbnail.dtype}]
            
            # Save with provided metadata
            description = descriptions[i] if i < len(descriptions) else "Halftone pattern"
            tiff.write(np.array(img_with_text), compression='jpeg2000', subifds=subifds, metadata={'description': description})
            tiff.write(thumbnail, subfiletype=1, compression='jpeg')

# Parameters for each image
width, height = 300, 300
pattern_densities = [0, 1, 2]  # Different densities for different halftone patterns

# Generate multiple halftone patterns
halftone_images = [generate_halftone_pattern(width, height, pd) for pd in pattern_densities]

# Descriptions for each pattern
descriptions = [f"Pattern with density {pd}" for pd in pattern_densities]

# Save the images with thumbnails as subIFDs and additional metadata
save_with_subifds_and_metadata(halftone_images, './tmp/multipage_halftone_example_with_icc_and_text.tiff', descriptions)

print("Multi-page TIFF file with JPEG 2000 compression, ICC profiles, text, and thumbnails in subIFDs has been saved.")
from PIL import Image, ImageDraw, ExifTags, TiffImagePlugin
import io

def create_hierarchical_image_with_subsampling_huffman_jfif_exif(filename, size=(800, 600), subsampling='4:2:0'):
    # Create the base image
    base_image = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(base_image)
    
    # Add some base content to the image
    draw.rectangle([10, 10, size[0]-10, size[1]-10], outline=(0, 0, 0), width=5)
    draw.text((20, 20), "Hierarchical Storage with Chroma Subsampling, Huffman Coding, JFIF and EXIF 2.31", fill=(0, 0, 0))
    
    # Function to recursively add smaller images
    def add_smaller_images(image, level=1):
        if level > 3:  # Limit the recursion depth to avoid too many small images
            return image
        smaller_image = image.copy().resize((int(image.width / 2), int(image.height / 2)))
        image.paste(smaller_image, (image.width - smaller_image.width, image.height - smaller_image.height))
        return add_smaller_images(image, level + 1)
    
    # Apply the smaller images onto the base image
    final_image = add_smaller_images(base_image)
    
    # Prepare EXIF data including tags for new features compatible with EXIF 2.31
    exif_data = TiffImagePlugin.ImageFileDirectory_v2()
    for tag, value in ExifTags.TAGS.items():
        if value == "DateTime":
            exif_data[tag] = '2023:01:01 00:00:00'  # Example date
            break
    
    # Convert EXIF data to bytes
    exif_bytes = exif_data.tobytes()
    
    # Save the image with Chroma Subsampling, enable optimized saving for Huffman Coding,
    # and ensure it's saved in the JFIF format by specifying the 'dpi' parameter, and include EXIF data for EXIF 2.31 compatibility.
    if subsampling == '4:4:4':
        final_image.save(filename, quality=95, subsampling=0, optimize=True, dpi=(72, 72), exif=exif_bytes)
    elif subsampling == '4:2:2':
        final_image.save(filename, quality=95, subsampling=1, optimize=True, dpi=(72, 72), exif=exif_bytes)
    elif subsampling == '4:2:0':
        final_image.save(filename, quality=95, subsampling=2, optimize=True, dpi=(72, 72), exif=exif_bytes)
    else:
        # Default to no subsampling if an unrecognized value is provided, but still enable Huffman Coding through optimization,
        # ensure JFIF format, and add EXIF data for EXIF 2.31 compatibility
        final_image.save(filename, optimize=True, dpi=(72, 72), exif=exif_bytes)

# Ensure the tmp directory exists
import os
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create and save the hierarchical image with Chroma Subsampling, Huffman Coding, JFIF Format, and EXIF 2.31 compatibility
create_hierarchical_image_with_subsampling_huffman_jfif_exif('./tmp/hierarchical_storage_with_subsampling_huffman_jfif_exif.jpg')
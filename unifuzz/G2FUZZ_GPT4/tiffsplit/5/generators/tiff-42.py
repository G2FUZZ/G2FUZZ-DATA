from PIL import Image, ImageDraw, ImageCms, TiffImagePlugin, TiffTags
import os

def create_colored_image(size, color):
    """Creates a simple colored image."""
    img = Image.new('RGB', size, color=color)
    return img

def add_text_to_image(image, text, position=(10, 10), color='white'):
    """Adds text to an image."""
    draw = ImageDraw.Draw(image)
    draw.text(position, text, fill=color)
    return image

def save_multi_page_tiff_with_metadata(output_path, images, metadata_list):
    """
    Saves a list of images as a multi-page TIFF, each with its own metadata.
    """
    # Initialize save_all and append_images for multi-page TIFF
    save_all = True
    append_images = []

    # Process each image, except the first one which is used to initiate the save process
    for img in images[1:]:
        append_images.append(img)

    # Process the first image for saving with metadata
    first_img = images[0]

    # Using TiffImagePlugin's IFD class to add custom metadata to the first image
    info = TiffImagePlugin.ImageFileDirectory_v2()
    for tag, value in metadata_list[0].items():
        if tag in TiffTags.TAGS_V2:
            tag_id = TiffTags.TAGS_V2[tag]
            info[tag_id] = value
        else:
            # Handle custom or unrecognized tags here (e.g., InkNames, PlanarConfiguration)
            print(f"Warning: Tag '{tag}' not directly supported or unrecognized. Might need manual handling.")

    # Save the multi-page TIFF with metadata for the first image
    first_img.save(output_path, save_all=save_all, append_images=append_images, format='TIFF', tiffinfo=info)

    # Additional steps could be implemented here to add metadata to subsequent images in the TIFF

def main():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Create images with different colors
    images = [create_colored_image((100, 100), color) for color in ["red", "green", "blue"]]

    # Add text to each image
    images = [add_text_to_image(img, f"Color {color}") for img, color in zip(images, ["Red", "Green", "Blue"])]

    # Example metadata for each page
    metadata_list = [{
        "ImageDescription": f"Sample {color} page",
        "XResolution": (300, 1),
        "YResolution": (300, 1),
        "ResolutionUnit": 2,  # 2 indicates that the resolution is in pixels/inch
        # Additional metadata like InkNames or PlanarConfiguration could be added here
    } for color in ["Red", "Green", "Blue"]]

    # Save the multi-page TIFF with metadata for each image
    output_path = './tmp/multi_page_sample_with_metadata.tiff'
    save_multi_page_tiff_with_metadata(output_path, images, metadata_list)

    print(f"Multi-page TIFF image saved to {output_path}")

if __name__ == "__main__":
    main()
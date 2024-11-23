from PIL import Image, ImageCms, ImageDraw, PngImagePlugin
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

def save_multi_page_tiff(output_path, images, icc_profiles, metadata_list):
    """
    Saves a list of images as a multi-page TIFF, each with its own ICC profile and metadata.
    """
    # Initialize save_all and append_images for multi-page TIFF
    save_all = True
    append_images = []
    
    # Process each image, except the first one which is used to initiate the save process
    for i, img in enumerate(images[1:], start=1):
        # Convert PIL image to have the ICC profile embedded
        output_img = ImageCms.profileToProfile(img, icc_profiles[i], icc_profiles[i], outputMode='RGB')
        # Add metadata if provided
        if metadata_list and len(metadata_list) > i:
            output_img.info['Description'] = metadata_list[i]
        append_images.append(output_img)

    # Process the first image
    first_img = ImageCms.profileToProfile(images[0], icc_profiles[0], icc_profiles[0], outputMode='RGB')
    # Add metadata to the first image if provided
    if metadata_list:
        first_img.info['Description'] = metadata_list[0]
    
    # Save the multi-page TIFF
    first_img.save(output_path, save_all=save_all, append_images=append_images, format='TIFF')

def main():
    # Ensure the tmp directory exists
    output_dir = './tmp/'
    os.makedirs(output_dir, exist_ok=True)

    # Create images with different colors and sizes
    images = [create_colored_image((100 + i * 50, 100 + i * 50), color) for i, color in enumerate(["blue", "red", "green"])]

    # Add text to each image
    images = [add_text_to_image(img, f"Page {i+1}") for i, img in enumerate(images)]

    # Load a standard sRGB ICC profile for simplicity, but in real applications, you might use different profiles
    icc_profile = ImageCms.createProfile("sRGB")

    # Same ICC profile for simplicity; in a real scenario, you might have different profiles for each image
    icc_profiles = [icc_profile for _ in images]

    # Example metadata for each page
    metadata_list = [f"This is page {i+1}" for i in range(len(images))]

    # Save the multi-page TIFF
    output_path = os.path.join(output_dir, 'complex_image_with_icc.tiff')
    save_multi_page_tiff(output_path, images, icc_profiles, metadata_list)

    # Corrected the typo in the variable name here
    print(f"Multi-page TIFF image saved to {output_path}")

if __name__ == "__main__":
    main()
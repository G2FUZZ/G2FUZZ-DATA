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

    print(f"Multi-page TIFF image saved to {output_path}")
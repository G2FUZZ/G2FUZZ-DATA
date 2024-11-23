def save_image_with_complex_structure():
    base_path = './tmp/complex_images'
    # Ensure the base directory exists
    os.makedirs(base_path, exist_ok=True)  # Corrected variable name here

    image_size = (800, 600)
    compression_levels = [10, 50, 75, 95]

    for level in compression_levels:
        # Create a new image
        image = Image.new('RGB', image_size, color='blue')
        draw = ImageDraw.Draw(image)

        # Add complex drawing
        create_complex_image(draw)

        # Generate a directory for the current compression level
        dir_path = create_directory_structure(base_path, level)

        # Save the image with the specified compression level
        filename = os.path.join(dir_path, f'sample_complex_{level}.jpg')
        image.save(filename, 'JPEG', quality=level)
        print(f"Image saved at {filename}")
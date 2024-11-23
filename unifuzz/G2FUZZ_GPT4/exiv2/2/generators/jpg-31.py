def save_images_in_structure(images, base_dir='./tmp/'):
    """Save images in a structured directory format based on their properties."""
    os.makedirs(base_dir, exist_ok=True)
    for img_info in images:
        # Directory structure: ./tmp/{quality}/{color}/
        dir_path = os.path.join(base_dir, str(img_info['quality']), img_info['color'])
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, img_info['filename'])
        img_info['image'].save(file_path, 'JPEG')
        print(f"Saved: {file_path}")

# The rest of the code remains unchanged.
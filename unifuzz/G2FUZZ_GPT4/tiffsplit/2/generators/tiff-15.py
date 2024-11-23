from PIL import Image, ImageDraw

def create_pyramidal_tiff(save_path, base_image_size=(100, 100), base_drawing=((10, 90), (90, 90), (50, 10))):
    """
    Create a pyramidal TIFF image with multiple layers of decreasing resolutions.
    """
    # Create the base image
    base_image = Image.new("RGB", base_image_size, "white")
    draw = ImageDraw.Draw(base_image)
    draw.polygon(base_drawing, fill="blue")

    # Define different sizes for the pyramidal layers (50%, 25%, 12.5% of the original)
    sizes = [
        (int(base_image_size[0] * 0.5), int(base_image_size[1] * 0.5)),
        (int(base_image_size[0] * 0.25), int(base_image_size[1] * 0.25)),
        (int(base_image_size[0] * 0.125), int(base_image_size[1] * 0.125))
    ]

    # Create a list to hold each layer of the pyramid
    images = [base_image]  # Start with the base image

    # Generate the pyramidal layers
    for size in sizes:
        image = base_image.resize(size, Image.Resampling.LANCZOS)  # Updated to use Image.Resampling.LANCZOS
        images.append(image)

    # Save the image with the pyramidal layers
    base_image.save(
        save_path,
        format="TIFF",
        save_all=True,
        append_images=images[1:],  # Pass the additional images as a sequence
        compression="tiff_deflate",  # Compression scheme that works well for pyramidal TIFF
        dpi=(300, 300),
        resolution_unit=2
    )

# Adjusted example usage to save in the ./tmp/ directory
save_directory = "./tmp/"
save_path = f"{save_directory}pyramidal_tiff_example.tiff"
create_pyramidal_tiff(save_path)
print("Pyramidal TIFF image generated and saved in ./tmp/")
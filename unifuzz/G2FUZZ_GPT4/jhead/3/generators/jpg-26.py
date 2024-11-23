from PIL import Image, PngImagePlugin
import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a primary image (a simple blue square)
primary_image = Image.new('RGB', (800, 600), color='blue')

# Save the primary image with a placeholder for the Exif data
primary_image_path = os.path.join(output_dir, "image_with_complex_structure.jpg")
primary_image.save(primary_image_path, "JPEG")

# Function to embed basic metadata into the image
def embed_basic_metadata(image_path, metadata):
    # Load the primary image
    with Image.open(image_path) as img:
        # Initialize PngInfo for storing metadata (though saving as JPEG)
        pnginfo = PngImagePlugin.PngInfo()

        # Embed custom metadata
        for key, value in metadata.items():
            pnginfo.add_text(key, value)

        # Save the image with the new metadata
        img.save(image_path, "JPEG", pnginfo=pnginfo)

# Custom metadata to embed
custom_metadata = {
    "Author": "John Doe",
    "Description": "A blue square with complex Exif data."
}

# Embed the basic metadata into the primary image
embed_basic_metadata(primary_image_path, custom_metadata)

print("The basic metadata has been successfully embedded.")
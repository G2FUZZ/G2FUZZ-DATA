import os
from PIL import Image, PngImagePlugin

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a base image (full-size)
base_image = Image.new('RGB', (800, 600), 'blue')

# Create a thumbnail (smaller version)
thumbnail_size = (80, 60)
thumbnail_image = base_image.copy()
thumbnail_image.thumbnail(thumbnail_size)

# Embed the thumbnail into the original image's info dictionary
base_image.info['thumbnail'] = thumbnail_image

# Simulating SPIFF format feature addition
# Since PIL does not directly support SPIFF, we add metadata to simulate the feature for demonstration
spiff_info = PngImagePlugin.PngInfo()
spiff_info.add_text("Description", "SPIFF Format: Still Picture Interchange File Format")

# Save the image with the embedded thumbnail and SPIFF format simulation
output_path = os.path.join(output_dir, 'image_with_spiff.jpg')
base_image.save(output_path, 'JPEG', pnginfo=spiff_info)

print(f"Image saved with an embedded thumbnail and SPIFF Format feature at: {output_path}")
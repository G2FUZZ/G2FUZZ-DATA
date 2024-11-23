from PIL import Image

# Create a new red image
image = Image.new('RGB', (100, 100), "red")

# Save the image with gamma correction
gamma_value = 2.2
output_path = './tmp/gamma_corrected_image.png'
image.save(output_path, pnginfo=None, gamma=gamma_value)

print(f"Image saved with gamma correction ({gamma_value}) at {output_path}")
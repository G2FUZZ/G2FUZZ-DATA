from PIL import Image

# Create a new image with RGB mode
new_image = Image.new("RGB", (100, 100))

# Save the image with compression
compression_methods = ['LZW', 'ZIP', 'JPEG']
for method in compression_methods:
    new_image.save(f'./tmp/compressed_image_{method.lower()}.tiff', compression=method)

print("TIFF files with different compression methods have been generated and saved.")
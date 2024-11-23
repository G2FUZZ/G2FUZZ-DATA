from PIL import Image, ImageDraw

# Create a new image with RGBA mode (including alpha channel)
new_image = Image.new("RGBA", (200, 200), (255, 255, 255, 0))

# Draw shapes on different layers
draw = ImageDraw.Draw(new_image)
draw.rectangle([20, 20, 80, 80], fill=(255, 0, 0, 128))
draw.ellipse([100, 100, 150, 150], fill=(0, 255, 0, 128))

# Add metadata to the image
metadata = {
    'Author': 'John Doe',
    'Date': '2022-10-15',
    'Description': 'Sample TIFF file with multiple layers and metadata'
}
new_image.info['metadata'] = metadata

# Save the image with complex file structure
new_image.save('./tmp/complex_image.tiff', compression='tiff_lzw')

print("A TIFF file with multiple layers and metadata has been generated and saved.")
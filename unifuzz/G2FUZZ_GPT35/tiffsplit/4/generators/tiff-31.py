from PIL import Image, ImageDraw, TiffTags

# Create a new image with RGBA mode and add multiple layers
image = Image.new('RGBA', (200, 200), (255, 255, 255, 255))
layer1 = Image.new('RGBA', (200, 200), (255, 0, 0, 128))
layer2 = Image.new('RGBA', (200, 200), (0, 255, 0, 128))

# Add text to one of the layers
draw = ImageDraw.Draw(layer2)
draw.text((50, 50), "Complex TIFF Image", fill=(0, 0, 0, 255))

# Create a TIFF file with multiple layers and metadata
tiff_file = './tmp/complex_tiff_file.tiff'
image.save(tiff_file, compression='tiff_adobe_deflate', save_all=True, append_images=[layer1, layer2])

# Add metadata to the TIFF file
metadata = {
    270: "Complex TIFF Example",  # Tag for XPTitle
    270: "This is a sample TIFF file with multiple layers and metadata."  # Tag for ImageDescription
}
with Image.open(tiff_file) as tiff_image:
    tiff_image.save(tiff_file, tiffinfo=metadata)

print("Complex TIFF file with multiple layers and metadata has been saved in ./tmp/")
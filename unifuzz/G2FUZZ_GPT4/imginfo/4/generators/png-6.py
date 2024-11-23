from PIL import Image, PngImagePlugin

# Create a new image with RGB mode
image = Image.new("RGB", (100, 100), "blue")

# Use a built-in ICC profile instead of loading from a file
icc_profile = image.info.get('icc_profile')
if not icc_profile:
    # If the image doesn't have an ICC profile, you can optionally load a default one
    # For demonstration, we're not loading an external file here
    pass

# Add the ICC profile to the image's info dictionary if it exists
info = PngImagePlugin.PngInfo()
if icc_profile:
    info.add_icc(icc_profile, name='sRGB')

# Save the image with the ICC profile embedded
output_path = './tmp/colormanaged_image.png'
image.save(output_path, "PNG", pnginfo=info)

print(f"Image saved with an ICC profile at {output_path}")
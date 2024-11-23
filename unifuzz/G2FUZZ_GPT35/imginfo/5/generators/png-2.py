from PIL import Image

# Create a new RGBA image with transparency support
image = Image.new("RGBA", (100, 100), (0, 0, 0, 0))

# Save the image as a PNG file
image.save("./tmp/transparent_image.png", "PNG")
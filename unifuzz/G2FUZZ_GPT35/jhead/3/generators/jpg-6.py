from PIL import Image

# Create a solid color image
width, height = 100, 100
color = (255, 0, 0)  # Red color
image = Image.new("RGB", (width, height), color)

# Save the image with chroma subsampling
image.save("./tmp/chroma_subsampling.jpg", subsampling=0)
from PIL import Image, ImageDraw

# Create a new image with RGB mode and size 100x100
image = Image.new('RGB', (100, 100))

# Draw a white background
draw = ImageDraw.Draw(image)
draw.rectangle([(0, 0), (100, 100)], fill="white")

# Save the image with different quality levels
quality_levels = [50, 70, 90, 100]

for i, quality in enumerate(quality_levels):
    filename = f"./tmp/image_quality_{i+1}.jpg"
    image.save(filename, quality=quality)

print("Images saved with different quality levels.")
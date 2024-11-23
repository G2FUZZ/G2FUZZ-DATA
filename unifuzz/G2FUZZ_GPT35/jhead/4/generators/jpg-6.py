from PIL import Image

# Create a new image with a solid color
width, height = 200, 200
color = (255, 0, 0)  # Red color
image = Image.new("RGB", (width, height), color)

# Save image with different quality settings
quality_values = [10, 50, 80, 100]
for idx, quality in enumerate(quality_values):
    file_path = f"./tmp/image_quality_{quality}.jpg"
    image.save(file_path, quality=quality)
    print(f"Image saved with quality {quality} at {file_path}")
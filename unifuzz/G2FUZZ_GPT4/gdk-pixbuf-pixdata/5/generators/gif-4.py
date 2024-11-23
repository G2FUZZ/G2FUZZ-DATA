from PIL import Image, ImageDraw

# Create a new image with RGBA (Red, Green, Blue, Alpha) mode for transparency
img_size = (200, 200)
img = Image.new("RGBA", img_size)

# Use ImageDraw to create a simple shape with transparency
draw = ImageDraw.Draw(img)

# Draw a blue rectangle without transparency
draw.rectangle([50, 50, 150, 150], fill=(0, 0, 255, 255))

# Draw a red circle with transparency
# The fourth value in the fill color (150) specifies the transparency.
# 255 is fully opaque, 0 is fully transparent.
draw.ellipse([70, 70, 130, 130], fill=(255, 0, 0, 150))

# Convert the image to use a palette (P mode) which is necessary for GIFs
img = img.convert("RGBA").quantize()

# Save the image with transparency
output_path = './tmp/transparent_gif.gif'
img.save(output_path)

print(f"GIF saved to {output_path}")
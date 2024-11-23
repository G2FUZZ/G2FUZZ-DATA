from PIL import Image, ImageDraw

# Create a new transparent image
img_size = (200, 200)
transparent_image = Image.new("RGBA", img_size, (0, 0, 0, 0))

# Draw a semi-transparent square
draw = ImageDraw.Draw(transparent_image)
draw.rectangle([50, 50, 150, 150], fill=(255, 0, 0, 128))  # Red, half-transparent

# Convert to 'P' mode with transparency for saving as GIF
transparent_image = transparent_image.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=255)
# Transparency index is 0 in the palette
mask = Image.new("L", img_size, 0)
draw = ImageDraw.Draw(mask)
draw.rectangle([50, 50, 150, 150], fill=255)  # White area represents the opaque part
transparent_image.paste(255, mask=mask)  # 255 is the index of the transparent color in the palette

# Save the image
output_path = "./tmp/transparent_example.gif"
transparent_image.save(output_path, transparency=255)
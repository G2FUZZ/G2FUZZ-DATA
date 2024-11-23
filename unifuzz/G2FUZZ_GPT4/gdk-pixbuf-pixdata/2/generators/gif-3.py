from PIL import Image, ImageDraw

# Create a new image with RGBA (Red, Green, Blue, Alpha) mode for transparency
img_size = (200, 200)
transparent_color = (0, 0, 0, 0)  # RGBA where A=0 means fully transparent
solid_color = (255, 0, 0, 255)  # Red, fully opaque

# Create an image with a transparent background
image = Image.new("RGBA", img_size, transparent_color)

# Draw a red rectangle on the image
draw = ImageDraw.Draw(image)
rectangle_size = (50, 50, 150, 150)
draw.rectangle(rectangle_size, fill=solid_color)

# Convert the RGBA image to P mode which is required for GIFs, including transparency
# Note: The first color in the palette becomes the transparent one if no transparency is specified
# Therefore, we append the transparent color first
transparent_image = Image.new("RGBA", img_size, transparent_color)
transparent_image.paste(image, (0, 0), image)
p_image = transparent_image.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=255)

# Specify transparency index as 0 since it's the color we added first
p_image.info['transparency'] = 0

# Save the image
output_path = './tmp/transparent_gif.gif'
p_image.save(output_path, save_all=True, transparency=0)

print(f"Generated GIF saved to {output_path}")
from PIL import Image, ImageDraw

# Create a new image with a limited color palette
image = Image.new("P", (100, 100), 0)
draw = ImageDraw.Draw(image)
draw.rectangle([0, 0, 100, 100], fill=1)
draw.rectangle([10, 10, 90, 90], fill=2)

# Apply dithering to simulate colors not available in the palette
image = image.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=256)

# Save the image as a GIF file
image.save("./tmp/dithering.gif")
from PIL import Image, ImageDraw

# Create a white canvas
width, height = 100, 100
image = Image.new("RGB", (width, height), "white")

# Draw a black square in the middle
draw = ImageDraw.Draw(image)
square_size = 50
x0 = (width - square_size) // 2
y0 = (height - square_size) // 2
x1 = x0 + square_size
y1 = y0 + square_size
draw.rectangle([x0, y0, x1, y1], fill="black")

# Save the image as a GIF file
image.save("./tmp/lossless_compression.gif", "GIF")
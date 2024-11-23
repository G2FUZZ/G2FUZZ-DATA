import png

# Define the image properties
width = 100
height = 100

# Create a new PNG image
image = png.Writer(width=width, height=height, greyscale=True)

# Define the data for the image
data = []
for y in range(height):
    row = []
    for x in range(width):
        if x < 50:
            row.append(255)  # White color for the left half
        else:
            row.append(0)  # Black color for the right half
    data.append(row)

# Save the image to a file
with open('./tmp/extensible.png', 'wb') as f:
    image.write(f, data)
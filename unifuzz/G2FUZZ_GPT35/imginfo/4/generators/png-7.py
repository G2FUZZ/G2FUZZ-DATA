import png

# Create a PNG file with textual information
textual_info = "This is a PNG file with textual information."
file_path = "./tmp/textual_info.png"

with open(file_path, 'wb') as file:
    writer = png.Writer(1, 1, greyscale=False, bitdepth=8)
    writer.text = [('Description', textual_info)]
    writer.write(file, [[0, 0, 0]])  # Data should match the dimensions (1x1)

print(f"PNG file with textual information saved at {file_path}")
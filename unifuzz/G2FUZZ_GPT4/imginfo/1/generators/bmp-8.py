from PIL import Image

# Create an image with RGB mode
width, height = 100, 100
image = Image.new("RGB", (width, height), "white")

# Drawing a simple element with specific colors
# Here we're creating a gradient to demonstrate color management in a simplified manner
for i in range(width):
    for j in range(height):
        # Gradient from red to blue
        image.putpixel((i, j), (255, 255-int(255*(i/width)), int(255*(i/width))))

# Save the image with a specific file name in the ./tmp/ directory
file_path = './tmp/color_profile_demo.bmp'
image.save(file_path, "BMP")

print(f"BMP file saved to {file_path}")
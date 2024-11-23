from PIL import Image

# Create PNG files with different color depths
for color_depth in [1, 2, 4, 8, 16]:
    # Create a new image with RGBA mode
    image = Image.new("RGBA", (100, 100))

    # Save the image with the specified color depth
    image.save(f"./tmp/color_depth_{color_depth}.png", bit=1 << color_depth)

print("PNG files with different color depths have been generated and saved in the './tmp/' directory.")
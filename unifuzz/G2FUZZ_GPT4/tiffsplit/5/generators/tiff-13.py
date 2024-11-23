from PIL import Image, ImageDraw  # Import ImageDraw along with Image

# Define the image size and color (using an example color)
width, height = 800, 600
spot_color = (255, 100, 0)  # This is an orange color

# Create a new image with a white background
image = Image.new("RGB", (width, height), "white")

# Create a layer to represent the spot color
# For simplicity, we'll fill an area with the spot color
spot_layer = Image.new("RGB", (width, height), spot_color)
spot_mask = Image.new("L", (width, height), 0)  # Create a mask to define where the spot color is applied

# Now that ImageDraw is imported, this should work without error
spot_mask_draw = ImageDraw.Draw(spot_mask)
spot_mask_draw.ellipse((200, 150, 600, 450), fill=255)  # Example: Apply spot color in an elliptical area

# Combine the spot color layer with the main image using the mask
image.paste(spot_layer, (0, 0), spot_mask)

# Save the image as a TIFF file
output_path = "./tmp/spot_color_example.tiff"
image.save(output_path, "TIFF")

print(f"Spot color TIFF saved to {output_path}")
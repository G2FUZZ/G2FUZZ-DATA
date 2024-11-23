from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image to work with
image = Image.new('RGB', (800, 600), (255, 255, 255))
draw = ImageDraw.Draw(image)
draw.rectangle([200, 150, 600, 450], fill="skyblue", outline="black", width=3)
draw.text((300, 290), "Sample Image", fill="black")

# Create a thumbnail of the image
thumbnail_size = (80, 60)
thumbnail = image.copy()
thumbnail.thumbnail(thumbnail_size)

# Save the original image for reference (not necessary for the pixdata but useful for comparison)
image.save('./tmp/original_image.jpg')

# Save the thumbnail - in a real scenario, this could be embedded in a custom file format
thumbnail.save('./tmp/thumbnail.jpg')

# Simulate saving a 'pixdata' file with the thumbnail embedded
# For demonstration, we'll just concatenate some placeholder data with the thumbnail data
pixdata_filename = './tmp/sample.pixdata'
placeholder_data = b"This is placeholder data for the main content of the pixdata file.\n"
with open(pixdata_filename, 'wb') as pixdata_file:
    # Write the placeholder data
    pixdata_file.write(placeholder_data)
    # Embed the thumbnail data
    with open('./tmp/thumbnail.jpg', 'rb') as thumbnail_file:
        thumbnail_data = thumbnail_file.read()
        pixdata_file.write(thumbnail_data)

print(f"'pixdata' file with embedded thumbnail generated at: {pixdata_filename}")
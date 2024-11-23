from PIL import Image, ImageDraw
import piexif
import os

# Create an image with a gradient and add text
def create_gradient_with_text(width, height):
    image = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(image)
    
    for i in range(width):
        # Calculate the RGB values (simple gradient from black to red)
        rgb_value = int((i / width) * 255)
        draw.line((i, 0, i, height), fill=(rgb_value, 0, 0))
    
    # Adding text to the image
    d = ImageDraw.Draw(image)
    d.text((10, 10), "Hello, Gradient!", fill=(255, 255, 255))
    
    return image

# Create a gradient image with text
width, height = 800, 600  # Adjusted size
gradient_image_with_text = create_gradient_with_text(width, height)

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define complex EXIF data for the gradient image
exif_dict = {
    "0th": {
        piexif.ImageIFD.Make: "GradientMaker",  # Not an actual camera make
        piexif.ImageIFD.Model: "Gradient Model 1",  # Not an actual camera model
        piexif.ImageIFD.XResolution: (300, 1),
        piexif.ImageIFD.YResolution: (300, 1),
        piexif.ImageIFD.Software: "GradientEXIF",
        piexif.ImageIFD.DateTime: '2023:01:01 00:00:00'
    },
    "Exif": {},
    "GPS": {},
    "1st": {},
    "thumbnail": None,  # Will be filled with the thumbnail bytes
    "Interop": {},
}

# Generate a thumbnail for the gradient image
thumbnail = gradient_image_with_text.copy()
thumbnail.thumbnail((128, 128), Image.Resampling.LANCZOS)
exif_dict['thumbnail'] = thumbnail.tobytes("jpeg", "RGB")

# Convert the dictionary to bytes
exif_bytes = piexif.dump(exif_dict)

# Save the gradient image with complex EXIF data in a progressive JPEG format
gradient_image_with_text.save('./tmp/progressive_gradient_with_exif.jpg', 'JPEG', quality=80, progressive=True, exif=exif_bytes)

print("Gradient image with complex EXIF data saved.")
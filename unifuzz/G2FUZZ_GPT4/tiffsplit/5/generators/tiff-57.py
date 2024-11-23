from PIL import Image, ImageDraw, ImageFont
import os

# Function to create a simple image with a specified color and size
def create_image_with_color(color, size=(100, 100), text="", text_color="white"):
    # Create an RGB image with the specified background color
    image = Image.new("RGB", size, color=color)
    draw = ImageDraw.Draw(image)
    # Optionally, add text to the image
    if text:
        # Attempt to use a default font (this part may need adjustment based on your system and PIL version)
        try:
            font = ImageFont.truetype("arial.ttf", 15)
        except IOError:
            font = ImageFont.load_default()
        draw.text((10, 40), text, fill=text_color, font=font)
    return image

# Function to generate images with different properties
def generate_complex_tiff(filename="complex_structure.tiff"):
    # Creating a list of images with different properties
    images = [
        create_image_with_color("red", (100, 100), "Red Layer"),
        create_image_with_color("green", (200, 200), "Green Layer"),
        create_image_with_color("blue", (300, 300), "Blue Layer", text_color="yellow"),
        create_image_with_color("yellow", (400, 400), "Yellow Layer", text_color="black")
    ]

    # Save options to include metadata and use different compressions
    save_options = {
        "compression": "tiff_adobe_deflate",
        "resolution": (300.0, 300.0),
        "resolution_unit": 2  # 2 corresponds to dots per inch
    }

    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Save the first image to initiate the multi-page TIFF with specific save options
    images[0].save(f'./tmp/{filename}', **save_options)

    # Now, append the rest of the images with updated save options for each
    for img in images[1:]:
        save_options.update({
            "save_all": True,
            "append_images": [img]
        })
        img.save(f'./tmp/{filename}', **save_options)
    
    print(f"Complex TIFF structure has been saved as ./tmp/{filename}")

# Generating the TIFF with complex file structures
generate_complex_tiff("multi_page_with_complex_structures.tiff")
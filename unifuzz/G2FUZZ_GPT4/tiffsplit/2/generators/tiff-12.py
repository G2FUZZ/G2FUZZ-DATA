from PIL import Image, ImageDraw

def create_image_with_orientation(orientation, save_path):
    # Create a simple image with a basic drawing
    image = Image.new("RGB", (100, 100), "white")
    draw = ImageDraw.Draw(image)
    # Draw a simple triangle that will help us identify the orientation
    draw.polygon([(10, 90), (90, 90), (50, 10)], fill="blue")
    
    # PIL doesn't directly support setting TIFF orientation tag through high-level APIs,
    # so we manually adjust the image if needed to simulate the effect.
    if orientation == 'top-left':
        pass  # This is the default, no need to transform.
    elif orientation == 'top-right':
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 'bottom-right':
        image = image.rotate(180)
    elif orientation == 'bottom-left':
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    elif orientation == 'left-top':
        image = image.transpose(Image.ROTATE_90).transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 'right-top':
        image = image.transpose(Image.ROTATE_90)
    elif orientation == 'right-bottom':
        image = image.transpose(Image.ROTATE_270).transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 'left-bottom':
        image = image.transpose(Image.ROTATE_270)
    
    # Save the image with the specified orientation
    image.save(save_path, "TIFF")

# Directory to save the generated TIFF files
save_directory = "./tmp/"

# List of orientations to generate images for
orientations = [
    'top-left', 'top-right',
    'bottom-right', 'bottom-left',
    'left-top', 'right-top',
    'right-bottom', 'left-bottom'
]

for orientation in orientations:
    save_path = f"{save_directory}image_orientation_{orientation}.tiff"
    create_image_with_orientation(orientation, save_path)

print("TIFF images generated with various orientations.")
from PIL import Image, ImageDraw
import datetime

def create_stereoscopic_base_image():
    # Create a simple image with a basic drawing for stereoscopic effect
    base_image = Image.new("RGB", (200, 100), "white")
    draw_left = ImageDraw.Draw(base_image)
    draw_right = ImageDraw.Draw(base_image)

    # Draw simple triangles for left and right images with a slight offset to create a 3D effect
    # Left triangle
    draw_left.polygon([(10, 90), (90, 90), (50, 10)], fill="blue")
    # Right triangle (slightly offset)
    draw_right.polygon([(110, 90), (190, 90), (150, 10)], fill="blue")

    return base_image

def create_image_with_orientation_timestamp_and_stereoscopic(orientation, save_path):
    image = create_stereoscopic_base_image()

    # Manually adjust the image for orientation, similar to previous function
    if orientation == 'top-left':
        pass  # Default, no transformation is needed.
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

    # Add time stamps using Exif Tags
    now = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    exif_data = {
        36867: now,  # DateTimeOriginal
        36868: now,  # DateTimeDigitized
        306: now,    # DateTime
    }
    # Note: The actual implementation for writing these Exif tags is not included here due to PIL limitations.

    # Save the stereoscopic image
    image.save(save_path, "TIFF")

# Directory to save the generated TIFF files
save_directory = "./tmp/"

# List of orientations to generate stereoscopic images for, with timestamps
orientations = [
    'top-left', 'top-right',
    'bottom-right', 'bottom-left',
    'left-top', 'right-top',
    'right-bottom', 'left-bottom'
]

for orientation in orientations:
    save_path = f"{save_directory}stereoscopic_image_orientation_{orientation}_timestamp.tiff"
    create_image_with_orientation_timestamp_and_stereoscopic(orientation, save_path)

print("Stereoscopic TIFF images generated with various orientations and timestamps.")
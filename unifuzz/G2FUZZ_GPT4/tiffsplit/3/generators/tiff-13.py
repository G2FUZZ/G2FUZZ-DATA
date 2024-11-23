from PIL import Image, ImageDraw
import os

# Create a directory to store the generated TIFF file
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create a simple image with a single colored rectangle
def create_image(color, size=(100, 100)):
    image = Image.new('RGB', size, "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([10, 10, 90, 90], fill=color)
    return image

# Create a few images with different colors
images = [
    create_image('red'),
    create_image('green'),
    create_image('blue'),
    create_image('yellow')
]

# Define document scanning tags
document_scanning_tags = {
    "DocumentName": "Sample Document",
    "ImageDescription": "A collection of colored rectangles",
    "Make": "Virtual Scanner",
    "Model": "VS-100",
    "PageNumber": 1,
    "Software": "PIL"
}

# Prepare additional tags by mapping the tags to their corresponding TIFFTAG codes
# These codes are placeholders; you should replace them with the correct codes for real applications
additional_tags = [
    (269, document_scanning_tags["DocumentName"]),  # DocumentName tag
    (270, document_scanning_tags["ImageDescription"]),  # ImageDescription tag
    (271, document_scanning_tags["Make"]),  # Make tag
    (272, document_scanning_tags["Model"]),  # Model tag
    (297, (document_scanning_tags["PageNumber"], 0)),  # PageNumber tag (numerator, denominator)
    (305, document_scanning_tags["Software"]),  # Software tag
]

# Save the images as a multi-page TIFF with document scanning tags
images[0].save(
    os.path.join(output_dir, 'multi_page_with_tags.tiff'),
    save_all=True,
    append_images=images[1:],
    tiffinfo=dict(additional_tags)
)
from PIL import Image, ImageDraw, ImageCms
import os

# Create a directory to store the generated TIFF file
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Function to create a simple image with a single colored rectangle
def create_image(color, size=(100, 100), color_space='RGB'):
    if color_space == 'CIELab':
        # Create an image in RGB
        image = Image.new('RGB', size, "white")
        draw = ImageDraw.Draw(image)
        draw.rectangle([10, 10, 90, 90], fill=color)
        # Convert RGB image to CIELab
        srgb_profile = ImageCms.createProfile("sRGB")
        lab_profile = ImageCms.createProfile("LAB")
        rgb2lab_transform = ImageCms.buildTransformFromOpenProfiles(srgb_profile, lab_profile, "RGB", "LAB")
        image = ImageCms.applyTransform(image, rgb2lab_transform)
        return image
    else:
        # Default to RGB if not specified otherwise
        image = Image.new('RGB', size, "white")
        draw = ImageDraw.Draw(image)
        draw.rectangle([10, 10, 90, 90], fill=color)
        return image

# Create a few images with different colors and in CIELab color space for demonstration
images = [
    create_image('red', color_space='CIELab'),
    create_image('green', color_space='CIELab'),
    create_image('blue', color_space='CIELab'),
    create_image('yellow', color_space='CIELab')
]

# Define document scanning tags
document_scanning_tags = {
    "DocumentName": "Sample Document",
    "ImageDescription": "A collection of colored rectangles in CIELab color space",
    "Make": "Virtual Scanner",
    "Model": "VS-100",
    "PageNumber": 1,
    "Software": "PIL"
}

# Prepare additional tags by mapping the tags to their corresponding TIFFTAG codes
additional_tags = [
    (269, document_scanning_tags["DocumentName"]),  # DocumentName tag
    (270, document_scanning_tags["ImageDescription"]),  # ImageDescription tag
    (271, document_scanning_tags["Make"]),  # Make tag
    (272, document_scanning_tags["Model"]),  # Model tag
    (297, (document_scanning_tags["PageNumber"], 0)),  # PageNumber tag (numerator, denominator)
    (305, document_scanning_tags["Software"]),  # Software tag
    # Add a tag for Photometric Interpretation to indicate the use of CIELab (assuming 32803 is its code)
    # Note: 32803 is a placeholder and should be replaced with the correct code for CIELab if different
    (262, 32803) # Assuming 32803 is the code for CIELab Photometric Interpretation
]

# Save the images as a multi-page TIFF with document scanning tags, including Rich Photometric Interpretations
images[0].save(
    os.path.join(output_dir, 'multi_page_cielab_with_tags.tiff'),
    save_all=True,
    append_images=images[1:],
    tiffinfo=dict(additional_tags)
)
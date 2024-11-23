import os
import numpy as np
from PIL import Image
from tifffile import TiffWriter
import xml.etree.ElementTree as ET

# Function to create sample image arrays
def create_sample_image_array(width, height, color):
    """
    Create a NumPy array representing an image with a solid color.

    Args:
    - width (int): The width of the image.
    - height (int): The height of the image.
    - color (tuple): The color of the image (R, G, B).

    Returns:
    - image_array (numpy.ndarray): The created image as a NumPy array.
    """
    image = Image.new("RGB", (width, height), color=color)
    image_array = np.array(image)
    return image_array

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define dimensions and create a base image for each dimension
width, height, channels, timepoints = 1024, 1024, 3, 5
base_images = np.zeros((timepoints, channels, height, width, 3), dtype=np.uint8)

# Populate the base_images array with sample data
for t in range(timepoints):
    for c in range(channels):
        color = tuple(np.random.randint(0, 256, 3).tolist())  # Random color for each channel
        base_images[t, c] = create_sample_image_array(width, height, color)

# Generating OME-XML metadata
def generate_ome_xml(width, height, channels, timepoints):
    """
    Generate OME-XML metadata string for describing the image dimensions and structure.

    Args:
    - width (int): The width of the image.
    - height (int): The height of the image.
    - channels (int): The number of channels in the image.
    - timepoints (int): The number of time points in the image.

    Returns:
    - ome_xml_str (str): The OME-XML metadata as a string.
    """
    # Create an XML element for OME
    NS = "http://www.openmicroscopy.org/Schemas/OME/2016-06"
    E = ET.Element("OME", xmlns=NS)
    
    # Create an Image element for each time point
    for t in range(timepoints):
        image = ET.SubElement(E, "Image", ID=f"Image:{t}")
        pixels = ET.SubElement(image, "Pixels", ID=f"Pixels:{t}",
                               DimensionOrder="XYZCT",
                               Type="uint8",
                               SizeX=str(width),
                               SizeY=str(height),
                               SizeZ="1",
                               SizeC=str(channels),
                               SizeT="1")
        
        # Create a channel element for each channel
        for c in range(channels):
            ET.SubElement(pixels, "Channel", ID=f"Channel:{t}:{c}", SamplesPerPixel="1")
    
    # Convert to string
    ome_xml_tree = ET.ElementTree(E)
    ome_xml_str = ET.tostring(E, encoding='utf-8', method='xml').decode()
    return ome_xml_str

# Generate OME-XML metadata
ome_xml = generate_ome_xml(width, height, channels, timepoints)

# Save the images with OME-TIFF format
with TiffWriter('./tmp/complex_ome_tiff.tif', bigtiff=True) as tiff:
    for t in range(timepoints):
        for c in range(channels):
            image_data = base_images[t, c]
            if t == 0 and c == 0:  # Write OME-XML metadata to the first channel of the first time point
                tiff.write(image_data,
                           photometric='rgb',
                           metadata={'axes': 'YX'},
                           description=ome_xml)  # Include OME-XML metadata here
            else:
                tiff.write(image_data,
                           photometric='rgb',
                           metadata={'axes': 'YX'})

print("Complex OME-TIFF image with multi-channel, time-series data has been saved.")
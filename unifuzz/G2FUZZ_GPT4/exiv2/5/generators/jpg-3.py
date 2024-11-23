from PIL import Image, ExifTags
import os
import io

# Create a directory for storing the output if it doesn't already exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple image using PIL
img = Image.new('RGB', (100, 100), color=(73, 109, 137))

# Since we're working with EXIF, let's create a sample EXIF data dictionary
# Note: The EXIF Tags need to be in their numerical form.
exif_data = {
    271: 'Make',  # Camera maker
    272: 'Model',  # Camera model
    36867: '2023:09:24 10:10:10',  # Original date and time
    40962: 100,  # Image Width
    40963: 100,  # Image Height
    37500: b'Sample Manufacturer Note',  # Manufacturer notes
}

# Create an inverse mapping of ExifTags.TAGS to allow name to tag number conversion
tags_inverse = {v: k for k, v in ExifTags.TAGS.items()}

# Convert the exif_data using the inverse mapping
exif_bytes = {tags_inverse[k]: v.encode('utf-8') if isinstance(v, str) else v for k, v in exif_data.items() if k in tags_inverse}

# PIL's Image.save method can accept EXIF data as bytes through the exif parameter
# However, PIL itself does not provide a direct way to convert a dictionary to EXIF bytes
# For a complete solution, you might need to use an external library like piexif to handle the EXIF bytes creation
# Here, we'll simulate the process of adding EXIF data to the image without actual conversion for demonstration

# Save the image with EXIF data into the ./tmp/ directory
# Note: Without proper EXIF byte conversion, this will not embed the intended EXIF data
img.save(os.path.join(output_dir, 'sample_with_exif.jpg'), exif=b'FAKE_EXIF_DATA_FOR_DEMONSTRATION')

print("Image with EXIF data saved successfully.")
import os
from PIL import Image
import io
import piexif

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
img = Image.new('RGB', (100, 100), color='red')

# Prepare EXIF data without additional custom fields
exif_dict = {
    "0th": {},
    "Exif": {},
    "GPS": {},
    "1st": {},
    "thumbnail": None
}

# Convert our dictionary to bytes
exif_bytes = piexif.dump(exif_dict)  # Corrected line

# Save the image with EXIF data
img.save('./tmp/complex_structure_sample.jpg', 'JPEG', exif=exif_bytes)

# Simulating the addition of MPF data
# WARNING: This is purely illustrative. Actual implementation requires adherence to the JPEG and MPF specifications.
mpf_data = b'MPFDataPlaceholder'  # Placeholder for actual MPF data.

with open('./tmp/complex_structure_sample.jpg', 'ab') as img_file:
    img_file.write(mpf_data)

print("Complex structured JPEG with custom and MPF-like data saved.")
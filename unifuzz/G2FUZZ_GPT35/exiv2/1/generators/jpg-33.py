import os
from PIL import Image
from iptcinfo3 import IPTCInfo
from PIL.ExifTags import TAGS, GPSTAGS
import io

# Create a directory to save the generated jpg files
os.makedirs('./tmp/', exist_ok=True)

# Generate a jpg file with extended metadata
img = Image.new('RGB', (200, 200), color='green')
img.save('./tmp/example_extended.jpg')

# Add extended metadata to the jpg file
info = IPTCInfo('./tmp/example_extended.jpg', force=True)
info['keywords'] = ['example', 'metadata', 'jpg']
info['caption/abstract'] = 'This is an example of a jpg file with extended metadata.'
info['custom1'] = 'Additional IPTC metadata field 1'
info['custom2'] = 'Additional IPTC metadata field 2'
info.save()

# Add EXIF data to the jpg file
exif_data = {
    TAGS[key]: 'Value' if TAGS[key] != 'GPSInfo' else {
        GPSTAGS[gps_key]: 'GPS Value' for gps_key in value
    } for key, value in img.info.items() if key in TAGS
}

# Convert the exif dictionary to bytes
exif_bytes = {TAGS[key]: value for key, value in exif_data.items()}

# Save the image with the updated exif data
output = io.BytesIO()
img.save(output, format='JPEG', exif=bytes(str(exif_bytes), 'utf-8'))
output.seek(0)
img = Image.open(output)
img.save('./tmp/example_extended.jpg')
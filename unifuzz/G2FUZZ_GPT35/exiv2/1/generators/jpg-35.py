import os
from PIL import Image
from iptcinfo3 import IPTCInfo

# Create a directory to save the generated jpg files
os.makedirs('./tmp/', exist_ok=True)

# Generate a jpg file with more complex metadata structure
img = Image.new('RGB', (200, 200), color='green')
img.save('./tmp/complex_example.jpg')

# Add metadata to the jpg file
info = IPTCInfo('./tmp/complex_example.jpg', force=True)
info['keywords'] = ['complex', 'metadata', 'jpg']
info['caption/abstract'] = 'This is an example of a jpg file with complex metadata structure.'
info['custom1'] = 'Additional Metadata Field 1: Country/PrimaryLocationName'
info['custom2'] = 'Additional Metadata Field 2: City'
info['custom3'] = 'Additional Metadata Field 3: SpecialInstructions'
info['custom4'] = 'Additional Metadata Field 4: Headline'
info.save()
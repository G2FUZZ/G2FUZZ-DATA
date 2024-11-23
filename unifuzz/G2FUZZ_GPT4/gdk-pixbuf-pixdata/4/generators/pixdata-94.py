import os
import json
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected argument here

# Define a more complex structure for color profiles
color_data = {
    'metadata': {
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'version': '1.0',
        'description': 'A collection of color profiles categorized by usage'
    },
    'profiles': {
        'Photography': [
            {
                'name': 'Adobe RGB (1998)',
                'color_space': 'RGB',
                'purpose': 'Suitable for professional photography and printing with a wider gamut'
            },
            {
                'name': 'ProPhoto RGB',
                'color_space': 'RGB',
                'purpose': 'Extremely wide gamut suitable for high-end photography'
            }
        ],
        'Web & Digital Media': [
            {
                'name': 'sRGB IEC61966-2.1',
                'color_space': 'RGB',
                'purpose': 'Standard color space for internet and digital imaging'
            },
            {
                'name': 'Display P3',
                'color_space': 'RGB',
                'purpose': 'Digital cinema and HDR video, wider gamut than sRGB'
            }
        ],
        'Cinema': [
            {
                'name': 'DCI-P3',
                'color_space': 'RGB',
                'purpose': 'Standard for digital cinema'
            }
        ]
    }
}

# Save the complex color data as a pixdata file in JSON format
pixdata_file_path = './tmp/complex_color_profiles.pixdata'
with open(pixdata_file_path, 'w') as file:
    json.dump(color_data, file, indent=4, default=str)  # Use default=str to serialize datetime

print(f'Complex color profiles saved to {pixdata_file_path}')
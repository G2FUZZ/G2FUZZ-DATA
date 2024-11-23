import os
import json

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define color profile information (example data)
color_profiles = {
    'sRGB': {
        'profile_name': 'sRGB IEC61966-2.1',
        'color_space': 'RGB',
        'purpose': 'Standard color space for internet and digital imaging'
    },
    'Adobe RGB': {
        'profile_name': 'Adobe RGB (1998)',
        'color_space': 'RGB',
        'purpose': 'Suitable for professional photography and printing with a wider gamut'
    },
    'Display P3': {
        'profile_name': 'Display P3',
        'color_space': 'RGB',
        'purpose': 'Digital cinema and HDR video, wider gamut than sRGB'
    }
}

# Save the color profiles as a pixdata file in JSON format
pixdata_file_path = './tmp/color_profiles.pixdata'
with open(pixdata_file_path, 'w') as file:
    json.dump(color_profiles, file)

print(f'Color profiles saved to {pixdata_file_path}')
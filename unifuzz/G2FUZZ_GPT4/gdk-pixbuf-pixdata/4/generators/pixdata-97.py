import os
import json

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define complex color profile information with nested structures
color_profiles = {
    'sRGB': {
        'profile_name': 'sRGB IEC61966-2.1',
        'color_space': 'RGB',
        'purpose': 'Standard color space for internet and digital imaging',
        'color_values': {
            'red': [255, 0, 0],
            'green': [0, 255, 0],
            'blue': [0, 0, 255]
        },
        'usage_scenarios': ['web design', 'online media']
    },
    'Adobe RGB': {
        'profile_name': 'Adobe RGB (1998)',
        'color_space': 'RGB',
        'purpose': 'Suitable for professional photography and printing with a wider gamut',
        'color_values': {
            'red': [255, 0, 0],
            'green': [0, 255, 0],
            'blue': [0, 0, 255]
        },
        'usage_scenarios': ['professional photography', 'high-quality print']
    },
    'Display P3': {
        'profile_name': 'Display P3',
        'color_space': 'RGB',
        'purpose': 'Digital cinema and HDR video, wider gamut than sRGB',
        'color_values': {
            'red': [255, 0, 0],
            'green': [0, 255, 0],
            'blue': [0, 0, 255]
        },
        'usage_scenarios': ['digital cinema', 'HDR video']
    }
}

# Save the color profiles with complex structures as a pixdata file in JSON format
pixdata_file_path = './tmp/complex_color_profiles.pixdata'
with open(pixdata_file_path, 'w') as file:
    json.dump(color_profiles, file, indent=4)  # Use indent=4 for pretty-printing

print(f'Complex color profiles saved to {pixdata_file_path}')
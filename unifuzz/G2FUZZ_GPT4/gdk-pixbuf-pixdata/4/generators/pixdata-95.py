import os
import json

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define complex resolution information including multiple device types
resolution_data = {
    "devices": [
        {
            "type": "smartphone",
            "brand": "BrandX",
            "models": [
                {
                    "name": "ModelA",
                    "resolutions": [
                        {"dpi": 300, "width_pixels": 1080, "height_pixels": 1920, "description": "Full HD"},
                        {"dpi": 450, "width_pixels": 1440, "height_pixels": 2560, "description": "QHD"}
                    ]
                },
                {
                    "name": "ModelB",
                    "resolutions": [
                        {"dpi": 330, "width_pixels": 750, "height_pixels": 1334, "description": "Retina HD"}
                    ]
                }
            ]
        },
        {
            "type": "monitor",
            "brand": "BrandY",
            "models": [
                {
                    "name": "UltraView 32\"",
                    "resolutions": [
                        {"dpi": 140, "width_pixels": 3840, "height_pixels": 2160, "description": "4K UHD"}
                    ]
                },
                {
                    "name": "MegaDisplay 27\"",
                    "resolutions": [
                        {"dpi": 220, "width_pixels": 2560, "height_pixels": 1440, "description": "QHD"}
                    ]
                }
            ]
        }
    ]
}

# Save the complex resolution information into a pixdata file
file_path = './tmp/complex_resolution_info.pixdata'
with open(file_path, 'w') as file:
    json.dump(resolution_data, file, indent=4)  # Use indent for pretty printing

print(f'Complex resolution information saved in {file_path}')
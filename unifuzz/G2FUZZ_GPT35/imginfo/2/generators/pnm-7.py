import numpy as np

# Define the features content
features_content = "7. Widely Supported: PNM files are widely supported across various image processing software and platforms due to their simplicity and versatility."

# Function to generate PNM file
def generate_pnm_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

# Save the features to a PNM file
file_path = './tmp/features.pnm'
generate_pnm_file(file_path, features_content)
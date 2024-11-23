import os

# Define the features to be included in the pnm file
features = [
    "8. Cross-Platform Compatibility: 'pnm' files can be easily read and written across different platforms due to their simple and well-defined format."
]

# Create a directory to store the pnm files if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate pnm files with the specified features
for idx, feature in enumerate(features):
    filename = f'feature_{idx}.pnm'
    with open(os.path.join(output_dir, filename), 'w') as file:
        file.write(feature)

print("pnm files generated successfully in the ./tmp/ directory.")
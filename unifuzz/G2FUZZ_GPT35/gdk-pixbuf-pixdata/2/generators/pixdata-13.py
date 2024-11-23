import os

# Define the features
features = [
    "13. Annotations: Supports adding annotations or comments to the image data for additional information."
]

# Create the 'pixdata' files and save them in './tmp/'
os.makedirs('./tmp/', exist_ok=True)
for i, feature in enumerate(features):
    with open(f'./tmp/pixdata_{i + 1}.txt', 'w') as file:
        file.write(feature)
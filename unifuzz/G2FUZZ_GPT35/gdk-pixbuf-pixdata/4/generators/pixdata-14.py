import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp', exist_ok=True)

# Generate the pixdata files with the given features
features = "Text annotations: Support for adding textual information within the image file."
with open('./tmp/pixdata1.txt', 'w') as f:
    f.write(features)
with open('./tmp/pixdata2.txt', 'w') as f:
    f.write(features)

print("pixdata files generated and saved in ./tmp/ directory.")
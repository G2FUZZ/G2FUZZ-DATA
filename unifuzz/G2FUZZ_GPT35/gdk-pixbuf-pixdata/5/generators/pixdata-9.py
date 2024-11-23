import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with the specified features
with open('./tmp/pixdata1.txt', 'w') as f:
    f.write("Thumbnail: A smaller version of the image for preview purposes.")
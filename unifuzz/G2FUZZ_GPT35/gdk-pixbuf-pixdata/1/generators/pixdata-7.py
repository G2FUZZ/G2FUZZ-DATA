import os

# Create directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files
with open('./tmp/pixdata.txt', 'w') as file:
    file.write("Transparency information: Details about any transparency or alpha channel data present in the image.")
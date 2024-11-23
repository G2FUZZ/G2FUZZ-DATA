import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate raw pixel data
image_data = [0, 255, 100, 200, 150, 50, 75, 30, 180, 210]

# Save the raw pixel data to a file
with open('./tmp/pixdata.txt', 'w') as file:
    file.write('Image data: {}\n'.format(image_data))

print('pixdata file created successfully at ./tmp/pixdata.txt')
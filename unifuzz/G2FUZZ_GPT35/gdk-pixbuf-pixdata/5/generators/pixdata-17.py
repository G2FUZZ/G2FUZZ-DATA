import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pixdata files
features = "17. Interactivity: Features allowing user interaction with the image content, such as hotspots or clickable areas."

for i in range(3):  # Generate 3 pixdata files
    filename = directory + f'pixdata_{i + 1}.txt'
    with open(filename, 'w') as file:
        file.write(features)

print("Generated pixdata files successfully.")
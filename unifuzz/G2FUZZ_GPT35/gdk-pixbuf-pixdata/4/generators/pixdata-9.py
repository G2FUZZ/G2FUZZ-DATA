import os

# Define the features
features = "9. Layers: Ability to store and manipulate multiple layers of image data."

# Create a directory to store the files
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate the pixdata files
for i in range(3):
    filename = f'pixdata_{i + 1}.txt'
    with open(os.path.join(directory, filename), 'w') as file:
        file.write(features)

print("pixdata files generated successfully.")
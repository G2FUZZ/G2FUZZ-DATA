import os

# Define the features
features = "Layers: For multi-layer images, the file format may support storing and accessing multiple layers of image data."

# Create a directory to store the generated files
os.makedirs("./tmp", exist_ok=True)

# Save the features into a file named 'pixdata.txt' in the './tmp/' directory
with open("./tmp/pixdata.txt", "w") as file:
    file.write(features)

print("Generated 'pixdata' file saved successfully.")
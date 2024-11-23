import os

# Define the directory and filename
directory = "./tmp/"
filename = "image_resolution.pixdata"
filepath = os.path.join(directory, filename)

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Resolution information to be stored
resolution_info = {
    "width": 800,
    "height": 600
}

# Writing resolution information to the file
with open(filepath, "w") as file:
    file.write(f"Width: {resolution_info['width']} pixels\n")
    file.write(f"Height: {resolution_info['height']} pixels\n")

print(f"File '{filename}' with resolution information has been saved to '{directory}'.")
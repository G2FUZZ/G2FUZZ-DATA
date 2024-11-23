import os

# Define the features for the ras files
features = {
    "Format": "RAS (Sun Raster Image)"
}

# Create a directory to save the generated files
directory = "./tmp"
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate ras files with the specified features
for i in range(3):
    filename = f"file{i+1}.ras"
    with open(os.path.join(directory, filename), "w") as file:
        file.write("Features:\n")
        for key, value in features.items():
            file.write(f"{key}: {value}\n")
    print(f"Generated {filename}")

print("Files saved in ./tmp/ directory.")
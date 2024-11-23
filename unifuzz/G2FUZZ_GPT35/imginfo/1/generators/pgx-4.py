import os

# Define the features to be included in the pgx file
features = {
    "Color space": ["RGB", "CMYK", "grayscale"]
}

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pgx files with the specified features
for feature, color_spaces in features.items():
    file_name = f"{feature}.pgx"
    file_path = os.path.join(directory, file_name)
    
    with open(file_path, 'w') as file:
        file.write(f"Feature: {feature}\n")
        file.write("Supported color spaces:\n")
        for color_space in color_spaces:
            file.write(f"- {color_space}\n")

print("pgx files have been generated and saved in the 'tmp' directory.")
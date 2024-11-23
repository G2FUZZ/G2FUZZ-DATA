import os

# Define the extended features to be included in the 'pgx' files
extended_features = {
    "Layers": "pgx files may support multiple layers, enabling complex image compositions and editing capabilities.",
    "Metadata": "pgx files can store metadata such as author information, creation date, and image tags.",
    "Image Dimensions": "pgx files can store image dimensions, allowing for proper display and editing adjustment."
}

# Create the 'tmp' directory if it doesn't exist
os.makedirs("./tmp", exist_ok=True)

# Generate extended 'pgx' files
for feature, description in extended_features.items():
    filename = f"./tmp/{feature.lower().replace(' ', '_')}.pgx"
    with open(filename, "w") as file:
        file.write(f"Feature: {feature}\nDescription: {description}\n")
        if feature == "Metadata":
            file.write("Author: John Doe\nCreation Date: 2022-01-01\nTags: image, editing\n")
        elif feature == "Image Dimensions":
            file.write("Dimensions: 1920x1080\n")

print("Extended files generated successfully.")
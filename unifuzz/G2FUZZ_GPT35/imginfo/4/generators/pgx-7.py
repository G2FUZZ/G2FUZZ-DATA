import os

# Define the features to be included in the 'pgx' files
features = {
    "Layers": "pgx files may support multiple layers, enabling complex image compositions and editing capabilities."
}

# Create the 'tmp' directory if it doesn't exist
os.makedirs("./tmp", exist_ok=True)

# Generate 'pgx' files
for feature, description in features.items():
    filename = f"./tmp/{feature.lower()}.pgx"
    with open(filename, "w") as file:
        file.write(f"Feature: {feature}\nDescription: {description}\n")

print("Files generated successfully.")
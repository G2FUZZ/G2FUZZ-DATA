import os

# Define the metadata feature
metadata_feature = "5. Localization: XMP supports multilingual metadata descriptions to cater to different language requirements."

# Create a directory if it doesn't exist
directory = "./tmp/"
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP file with the metadata feature
xmp_filename = os.path.join(directory, "metadata_feature.xmp")
with open(xmp_filename, "w") as file:
    file.write(metadata_feature)

print(f"XMP file '{xmp_filename}' has been generated successfully.")
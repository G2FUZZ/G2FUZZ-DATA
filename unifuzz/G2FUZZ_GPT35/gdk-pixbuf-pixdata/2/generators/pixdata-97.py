import os
import datetime

# Define the features
features = """
Layers: For multi-layer images, the file format may support storing and accessing multiple layers of image data.
Metadata: Additional metadata is included to provide information about the image.
Timestamp: The timestamp of when the file is generated is added for reference.
"""

# Create a directory to store the generated files
os.makedirs("./tmp", exist_ok=True)

# Generate timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Save the features into a file named 'pixdata_extended.txt' in the './tmp/' directory with metadata and timestamp
with open("./tmp/pixdata_extended.txt", "w") as file:
    file.write(f"File Features:\n{features}\n\nMetadata:\nAuthor: John Doe\nDate Created: {timestamp}")

print("Generated 'pixdata_extended' file with additional features saved successfully.")
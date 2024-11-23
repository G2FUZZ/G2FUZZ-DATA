import os

# Create a directory to save the files
os.makedirs("./tmp/", exist_ok=True)

# Define the content to be written in the files
content = "7. Metadata: Allows for storing metadata information along with the image data."

# Generate and save the 'ras' files
for i in range(3):
    with open(f"./tmp/file{i + 1}.ras", "w") as file:
        file.write(content)

print("Files generated and saved successfully.")
import os

# Define the directory where the files will be saved
output_dir = "./tmp/"
# Ensure the directory exists
os.makedirs(output_dir, exist_ok=True)

# Define the filename and content
filename = "features.pgx"
content = """6. **Flexibility in Usage**: Although they are not as widely supported as other image formats like JPEG or PNG, PGX files can be used in specialized fields where image integrity and raw data manipulation are crucial, such as medical imaging, digital archiving, and scientific research."""

# Path to the file
file_path = os.path.join(output_dir, filename)

# Writing the content to the file
with open(file_path, "w") as file:
    file.write(content)

print(f"File saved to {file_path}")
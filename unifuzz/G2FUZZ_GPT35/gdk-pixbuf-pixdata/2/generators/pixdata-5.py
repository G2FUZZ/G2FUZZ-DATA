import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with the required features
metadata = {
    'image1': {'creation_date': '2022-01-15', 'author': 'John Doe', 'camera_settings': 'ISO 100, f/2.8'},
    'image2': {'creation_date': '2022-01-20', 'author': 'Jane Smith', 'camera_settings': 'ISO 200, f/4.0'}
}

for image_name, data in metadata.items():
    file_path = f'./tmp/{image_name}_pixdata.txt'
    with open(file_path, 'w') as file:
        file.write(f"Metadata for {image_name}:\n")
        file.write(f"Creation Date: {data['creation_date']}\n")
        file.write(f"Author: {data['author']}\n")
        file.write(f"Camera Settings: {data['camera_settings']}\n")

print("Pixdata files generated and saved in ./tmp/ directory.")
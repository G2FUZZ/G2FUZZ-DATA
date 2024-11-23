import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a PNM file with the specified feature
def generate_pnm_file(file_name, format_info):
    with open(f'./tmp/{file_name}.pnm', 'w') as file:
        file.write(f'P3\n# {format_info}\n1 1\n255\n255 255 255\n')

# Generate a PNM file with the specified features
generate_pnm_file('sample_pnm_file', 'Format: The PNM (Portable Any Map) format is a family of image file formats that can store images in either a binary or ASCII representation.')
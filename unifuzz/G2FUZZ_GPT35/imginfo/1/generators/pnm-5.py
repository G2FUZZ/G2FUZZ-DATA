import os

def generate_pnm_file(file_path, metadata):
    with open(file_path, 'w') as file:
        file.write("P3\n")
        file.write("# " + metadata + "\n")
        file.write("3 2\n")
        file.write("255\n")
        file.write("255 0 0\n")
        file.write("0 255 0\n")
        file.write("0 0 255\n")

# Create tmp directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

metadata = "Metadata: PNM files may contain optional metadata such as image dimensions and maximum color values."
file_path = './tmp/sample.pnm'
generate_pnm_file(file_path, metadata)

print(f"PNM file '{file_path}' generated successfully.")
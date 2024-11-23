import os

def generate_pnm_file(file_name, features):
    with open(file_name, 'w') as f:
        f.write("P3\n")
        f.write("# " + features + "\n")
        f.write("2 2\n")
        f.write("255\n")
        f.write("255 0 0\n")
        f.write("0 255 0\n")
        f.write("0 0 255\n")
        f.write("255 255 0\n")

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

file_name = "./tmp/example.pnm"
features = "Human Readable: The ASCII format of PNM files is human-readable, allowing users to inspect and modify the image data directly."
generate_pnm_file(file_name, features)
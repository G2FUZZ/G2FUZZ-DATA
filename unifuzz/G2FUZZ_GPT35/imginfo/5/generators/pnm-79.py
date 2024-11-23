import os

def generate_complex_pnm_file(file_name, features):
    with open(file_name, 'w') as f:
        f.write("P3\n")
        f.write("# " + features + "\n")
        f.write("3 3\n")
        f.write("255\n")
        f.write("255 0 0  # Red\n")
        f.write("0 255 0  # Green\n")
        f.write("0 0 255  # Blue\n")
        f.write("255 255 0  # Yellow\n")
        f.write("255 0 255  # Magenta\n")
        f.write("0 255 255  # Cyan\n")
        f.write("128 128 128  # Gray\n")
        f.write("255 255 255  # White\n")
        f.write("0 0 0  # Black\n")

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

file_name = "./tmp/complex_example.pnm"
features = "Complex File Structure: This file contains multiple color pixels and comments for each color."
generate_complex_pnm_file(file_name, features)
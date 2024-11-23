import os

def generate_pnm_file(file_name, width, height, max_pixel_value, pnm_format):
    header = f"{pnm_format}\n{width} {height}\n{max_pixel_value}\n"
    data = " ".join(["255"] * (width * height))  # Generating white image data
    
    with open(file_name, 'w') as file:
        file.write(header + data)

# Create a directory to save the generated files
os.makedirs("./tmp/", exist_ok=True)

# Generate PNM files
generate_pnm_file("./tmp/image1.pnm", 800, 600, 255, "P3")  # PPM format
generate_pnm_file("./tmp/image2.pnm", 640, 480, 1, "P1")  # PBM format
generate_pnm_file("./tmp/image3.pnm", 1024, 768, 4095, "P6")  # PPM format

print("PNM files generated successfully and saved in ./tmp/ directory.")
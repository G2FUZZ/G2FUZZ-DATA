import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'pnm' files with header information
def generate_pnm_file(width, height, max_pixel_value):
    file_name = f"./tmp/image_{width}x{height}.pnm"
    with open(file_name, 'w') as file:
        file.write(f"P3\n{width} {height}\n{max_pixel_value}\n")
        for _ in range(height):
            for _ in range(width):
                file.write("255 0 0\n")  # Example pixel value (red color)
    
    print(f"Generated {file_name}")

# Specify the header information for the 'pnm' files
width = 800
height = 600
max_pixel_value = 255

# Generate 'pnm' file with specified features
generate_pnm_file(width, height, max_pixel_value)
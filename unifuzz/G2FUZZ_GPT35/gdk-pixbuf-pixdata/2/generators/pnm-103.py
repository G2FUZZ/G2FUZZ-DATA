def generate_complex_pnm_file(file_path, width, height, pixels):
    with open(file_path, 'w') as file:
        file.write("P3\n")
        file.write("# Complex PNM file with multiple pixels and varying color intensities\n")
        file.write(str(width) + " " + str(height) + "\n")
        file.write("255\n")
        
        for pixel in pixels:
            file.write(" ".join(str(value) for value in pixel) + "\n")

# Define the content for the complex PNM file
complex_pnm_content = [
    [255, 0, 0],  # Red pixel
    [0, 255, 0],  # Green pixel
    [0, 0, 255],  # Blue pixel
    [255, 255, 0],  # Yellow pixel
    [128, 128, 128]  # Gray pixel
]

file_path_complex = './tmp/complex_sample.pnm'
generate_complex_pnm_file(file_path_complex, 3, 2, complex_pnm_content)
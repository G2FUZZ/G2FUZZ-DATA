import numpy as np

# Function to generate a TGA file with color correction information
def generate_tga_file(file_path):
    # Create a sample color correction matrix
    color_correction_matrix = np.array([[1.1, 0, 0],
                                        [0, 0.9, 0],
                                        [0, 0, 1.2]])
    
    # Save the color correction matrix to the file
    with open(file_path, 'wb') as file:
        file.write(color_correction_matrix.tobytes())

# Save the color correction information to a TGA file
file_path = './tmp/color_correction.tga'
generate_tga_file(file_path)
print(f'TGA file with color correction information saved at: {file_path}')
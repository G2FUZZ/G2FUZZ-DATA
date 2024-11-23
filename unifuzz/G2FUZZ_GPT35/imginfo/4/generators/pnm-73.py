import numpy as np

def generate_pnm_file(file_path, image_data, file_type='P2'):
    rows, cols, channels = image_data.shape
    max_val = np.max(image_data)

    with open(file_path, 'w') as f:
        f.write(f'{file_type}\n')
        f.write(f'{cols} {rows}\n')
        if file_type == 'P2' or file_type == 'P5':
            f.write(f'{max_val}\n')
        for i in range(rows):
            for j in range(cols):
                if file_type == 'P1' or file_type == 'P4':
                    f.write(f'{image_data[i, j, 0]} ')
                elif file_type == 'P2' or file_type == 'P5':
                    f.write(f'{image_data[i, j, 0]}\n')
                elif file_type == 'P3' or file_type == 'P6':
                    f.write(f'{image_data[i, j, 0]} {image_data[i, j, 1]} {image_data[i, j, 2]}\n')

# Define the dimensions of the image
rows = 100
cols = 100

# Generate random pixel values between 0 and 255 for a color image
pixels_color = np.random.randint(256, size=(rows, cols, 3))

# Generate random pixel values between 0 and 1 for a binary image
pixels_binary = np.random.randint(2, size=(rows, cols, 1))

# Save the pixel values to different types of PNM files
generate_pnm_file('./tmp/color_image.ppm', pixels_color, file_type='P3')
generate_pnm_file('./tmp/binary_image.pbm', pixels_binary, file_type='P1')
import numpy as np

def generate_pnm_file(file_path, image_data, file_type='P2'):
    rows, cols = image_data.shape
    max_val = np.max(image_data)

    with open(file_path, 'w') as f:
        f.write(f'{file_type}\n')
        f.write(f'{cols} {rows}\n')
        if file_type == 'P2' or file_type == 'P5':
            f.write(f'{max_val}\n')
        for i in range(rows):
            for j in range(cols):
                if file_type == 'P1' or file_type == 'P4':
                    f.write(f'{image_data[i, j]} ')
                elif file_type == 'P2' or file_type == 'P5':
                    f.write(f'{image_data[i, j]}\n')
                elif file_type == 'P3' or file_type == 'P6':
                    f.write(f'{image_data[i, j]} {image_data[i, j]} {image_data[i, j]}\n')

# Define the dimensions of the image
rows = 100
cols = 100

# Generate random pixel values between 0 and 255 for a grayscale image
pixels_gray = np.random.randint(256, size=(rows, cols))

# Save the pixel values to different types of PNM files
generate_pnm_file('./tmp/gray_image.pgm', pixels_gray, file_type='P2')
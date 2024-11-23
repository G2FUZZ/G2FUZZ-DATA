import numpy as np

def generate_pnm_file(file_path, image_data, file_type='P2'):
    rows, cols, *channels = image_data.shape
    max_val = np.max(image_data)

    with open(file_path, 'wb') as f:
        f.write(f'{file_type}\n'.encode())
        f.write(f'{cols} {rows}\n'.encode())
        if file_type in ['P2', 'P5']:
            f.write(f'{max_val}\n'.encode())
        for i in range(rows):
            for j in range(cols):
                if file_type in ['P1', 'P4']:
                    f.write(f'{image_data[i, j, 0]} '.encode())
                elif file_type in ['P2', 'P5']:
                    f.write(f'{image_data[i, j, 0]}\n'.encode())
                elif file_type in ['P3', 'P6']:
                    f.write(f'{image_data[i, j, 0]} {image_data[i, j, 1]} {image_data[i, j, 2]}\n'.encode())

# Create PNM files with different color depths
image_data_bw = np.zeros((10, 10, 1), dtype=np.uint8)  # Black and white image
generate_pnm_file('./tmp/black_white_image.pbm', image_data_bw, file_type='P1')

image_data_gray = np.zeros((10, 10, 1), dtype=np.uint8)  # Grayscale image
generate_pnm_file('./tmp/grayscale_image.pgm', image_data_gray, file_type='P2')

image_data_color = np.zeros((10, 10, 3), dtype=np.uint8)  # Color image
generate_pnm_file('./tmp/color_image.ppm', image_data_color, file_type='P3')
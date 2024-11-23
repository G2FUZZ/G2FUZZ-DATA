import numpy as np

def generate_pnm_file(file_path, image_data, file_type='P3'):
    rows = len(image_data)
    cols = len(image_data[0])

    with open(file_path, 'w') as f:
        f.write(f'{file_type}\n')
        f.write(f'{cols} {rows}\n')
        if file_type in ['P2', 'P3', 'P5', 'P6']:
            max_val = np.max(image_data)
            f.write(f'{max_val}\n')
        for i in range(rows):
            for j in range(cols):
                pixel_data = image_data[i][j]
                if len(pixel_data) == 1:  # Grayscale image
                    f.write(f'{pixel_data[0]} ')
                elif len(pixel_data) == 3:  # RGB image
                    f.write(f'{pixel_data[0]} {pixel_data[1]} {pixel_data[2]}\n')

# Generate PNM file content
pnm_content = """P3
# Example PNM file
3 2
255
255 0 0
0 255 0
0 0 255
255 255 0
255 255 255
0 0 0
"""

# Convert the PNM content to a list of lists for color image
pixels_color = [[list(map(int, line.split())) for line in pnm_content.splitlines()[3:]]]

# Save the pixel values to a PNM file
generate_pnm_file('./tmp/example.ppm', pixels_color, file_type='P3')
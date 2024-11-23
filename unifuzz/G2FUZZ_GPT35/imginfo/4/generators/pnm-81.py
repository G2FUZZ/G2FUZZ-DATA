import numpy as np

def generate_pnm_file(file_path, image_data, file_type='P3'):
    rows = len(image_data)
    cols = len(image_data[0])

    with open(file_path, 'w') as f:
        f.write(f'{file_type}\n')
        f.write(f'{cols} {rows}\n')
        if file_type in ['P1', 'P4']:
            for i in range(rows):
                for j in range(cols):
                    f.write(f'{image_data[i][j]} ')
        elif file_type in ['P2', 'P5']:
            max_val = np.max(image_data)
            f.write(f'{max_val}\n')
            for i in range(rows):
                for j in range(cols):
                    f.write(f'{image_data[i][j]}\n')
        elif file_type in ['P3', 'P6']:
            for row in image_data:
                for pixel in row:
                    f.write(f'{pixel} ')
                f.write('\n')

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
pixels_color = [list(map(int, line.split())) for line in pnm_content.splitlines()[3:]]

# Save the pixel values to a PNM file
generate_pnm_file('./tmp/example.ppm', pixels_color, file_type='P3')
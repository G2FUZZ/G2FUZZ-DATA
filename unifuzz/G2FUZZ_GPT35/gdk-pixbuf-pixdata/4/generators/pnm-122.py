import numpy as np

# Function to create a PNM file with extended metadata and comments
def create_extended_pnm_file(file_path, num_images=1, comments=None):
    width, height = 100, 100
    max_val = 255
    pixel_depth = 8

    if comments is None:
        comments = [
            "Extended PNM file with multiple images and comments",
            "Created using Python and numpy"
        ]

    for i in range(num_images):
        image_data = np.random.randint(0, max_val + 1, (height, width), dtype=np.uint8)

        with open(file_path + f'_{i}.pgm', 'wb') as f:
            f.write(b'P5\n')
            for comment in comments:
                f.write(f'# {comment}\n'.encode())
            f.write(f'{width} {height}\n'.encode())
            f.write(f'{max_val}\n'.encode())
            f.write(image_data.tobytes())

file_path = './tmp/extended_image'
create_extended_pnm_file(file_path, num_images=3)
print(f'Extended PNM files created and saved at: {file_path}_<index>.pgm')
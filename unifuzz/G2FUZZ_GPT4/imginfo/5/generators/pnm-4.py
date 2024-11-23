import os
import numpy as np

def generate_pnm_images():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Define image specifications
    image_specs = [
        # (width, height, maxval, filename)
        (100, 100, 255, 'image1.pnm'),  # Example of a PBM (Portable Bitmap) file if maxval is 1 or PGM file otherwise
        (200, 100, 255, 'image2.pnm'),  # Example of a PGM (Portable Graymap) file
        (100, 200, 255, 'image3.pnm')   # Example of a PPM (Portable Pixmap) file with different dimensions
    ]
    
    for width, height, maxval, filename in image_specs:
        # Generate a random image array
        # For PBM (maxval=1), use np.random.randint(0, 2, (height, width), dtype=np.uint8)
        # For PGM or PPM (maxval > 1), generate gray or RGB values respectively
        if maxval == 1:
            image_array = np.random.randint(0, 2, (height, width), dtype=np.uint8)
        else:
            # This example generates a grayscale image. For color, you would need a 3D array
            image_array = np.random.randint(0, maxval+1, (height, width), dtype=np.uint8)
        
        # Construct the header based on the maxval
        if maxval == 1:
            header = f'P1\n{width} {height}\n'
        elif maxval < 256:
            header = f'P5\n{width} {height}\n{maxval}\n'
        else:
            # This branch could be used for PPM or higher maxval PGM, but here we stick with PGM logic for simplicity
            header = f'P6\n{width} {height}\n{maxval}\n'
        
        # Write the PNM file
        with open(f'./tmp/{filename}', 'wb') as file:
            file.write(header.encode('ascii'))
            image_array.tofile(file)

generate_pnm_images()
import os
import numpy as np

def create_image(width, height, image_type='P1'):
    if image_type == 'P1':  # PBM
        return np.zeros((height, width), dtype=np.uint8)
    elif image_type == 'P2':  # PGM
        return np.zeros((height, width), dtype=np.uint8)
    elif image_type == 'P3':  # PPM
        return np.zeros((height, width, 3), dtype=np.uint8)  # 3 channels for RGB
    else:
        raise ValueError("Unsupported image type. Choose 'P1', 'P2', or 'P3'.")

def draw_rectangle(image, x, y, width, height, color):
    image[y:y+height, x:x+width] = color

def draw_circle(image, center_x, center_y, radius, color):
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if np.sqrt((center_x - x) ** 2 + (center_y - y) ** 2) <= radius:
                image[y, x] = color

def save_image(filename, image, image_type='P1'):
    height, width = image.shape[:2]
    max_val = 255 if image_type != 'P1' else None
    with open(filename, 'w') as f:
        f.write(f"{image_type}\n")
        f.write(f"{width} {height}\n")
        if max_val:
            f.write(f"{max_val}\n")
        if image_type == 'P3':  # PPM needs to flatten the 3D array
            for row in image:
                for pixel in row:
                    f.write(" ".join(map(str, pixel)) + " ")
                f.write("\n")
        else:  # PBM and PGM
            for row in image:
                f.write(" ".join(map(str, row)) + "\n")


# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Example usage
width, height = 100, 100  # Image dimensions
image_type = 'P3'  # 'P1' for PBM, 'P2' for PGM, 'P3' for PPM
image = create_image(width, height, image_type)

# Drawing a rectangle and circle on the image
draw_rectangle(image, 10, 10, 30, 50, color=(255, 0, 0) if image_type == 'P3' else 255)  # Red rectangle for PPM or white for others
draw_circle(image, 50, 50, 20, color=(0, 255, 0) if image_type == 'P3' else 128)  # Green circle for PPM or gray for PGM

# Path to save the PNM file
file_path = f'./tmp/sample.{image_type.lower()}'

# Save the image
save_image(file_path, image, image_type)

print(f"File saved to {file_path}")
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
        if image_type in ['P2', 'P3']:  # Include the max value for PGM and PPM
            f.write("# This is a {} file\n".format(image_type))
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

def main():
    output_dir = './tmp/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Define image dimensions and types
    width, height = 3, 3  # Image dimensions for simplicity
    image_types = ['P1', 'P2', 'P3']  # Image formats

    for image_type in image_types:
        image = create_image(width, height, image_type)
        if image_type == 'P1':  # Example drawing for PBM
            draw_rectangle(image, 0, 0, 3, 3, color=1)  # Simple example, fill all
        elif image_type == 'P2':  # Example drawing for PGM
            draw_rectangle(image, 0, 0, 3, 3, color=255)  # Simple example, fill all
        elif image_type == 'P3':  # Example drawing for PPM
            draw_rectangle(image, 0, 0, 3, 3, color=(255, 0, 0))  # Simple example, fill all red

        file_path = os.path.join(output_dir, f'image.{image_type.lower()}')
        save_image(file_path, image, image_type)
        print(f"File saved to {file_path}")

if __name__ == "__main__":
    main()
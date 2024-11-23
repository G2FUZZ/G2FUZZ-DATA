def generate_cross_pattern_ppm(image_width, image_height, cross_thickness):
    # Define colors
    black = "0 0 0 "
    white = "255 255 255 "

    # Create the PPM header
    header = f"P3\n{image_width} {image_height}\n255\n"
    
    # Initialize the image data
    image_data = []

    for y in range(image_height):
        row = []
        for x in range(image_width):
            # Check if the current pixel should be part of the cross
            if abs(x - image_width // 2) < cross_thickness // 2 or abs(y - image_height // 2) < cross_thickness // 2:
                row.append(white)
            else:
                row.append(black)
        image_data.append(''.join(row))

    # Combine the header and the image data
    ppm_data = header + '\n'.join(image_data)

    # Save the PPM data to a file
    with open('./tmp/cross_pattern.ppm', 'w') as f:
        f.write(ppm_data)

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate a PPM file with a simple cross pattern
generate_cross_pattern_ppm(100, 100, 10)
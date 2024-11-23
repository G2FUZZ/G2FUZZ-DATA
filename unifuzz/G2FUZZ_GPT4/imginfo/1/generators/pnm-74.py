import os

def create_gradient_ppm(width, height, output_file_path):
    """
    Create a PPM file with a horizontal RGB gradient.
    """
    ppm_header = f'P3\n{width} {height}\n255\n'
    ppm_data = ''
    for i in range(height):
        for j in range(width):
            red = int((j / width) * 255)
            green = int((i / height) * 255)
            blue = 255 - red
            ppm_data += f'{red} {green} {blue}  '
        ppm_data += '\n'
    
    ppm_content = ppm_header + ppm_data.strip()
    with open(output_file_path, 'w') as file:
        file.write(ppm_content)

def create_gradient_pgm(width, height, output_file_path):
    """
    Create a PGM file with a vertical grayscale gradient.
    """
    pgm_header = f'P2\n{width} {height}\n255\n'
    pgm_data = ''
    for i in range(height):
        gray_value = int((i / height) * 255)
        pgm_data += (' '.join([str(gray_value)] * width) + '\n')
    
    pgm_content = pgm_header + pgm_data.strip()
    with open(output_file_path, 'w') as file:
        file.write(pgm_content)

def generate_pnm(output_dir='./tmp/', filename='gradient', format='ppm', width=100, height=100):
    """
    Generate a PNM file (either PPM or PGM) with a gradient.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the file path based on the chosen format
    if format.lower() == 'ppm':
        output_file_path = os.path.join(output_dir, f'{filename}.ppm')
        create_gradient_ppm(width, height, output_file_path)
    elif format.lower() == 'pgm':
        output_file_path = os.path.join(output_dir, f'{filename}.pgm')
        create_gradient_pgm(width, height, output_file_path)
    else:
        print(f'Unsupported format: {format}')
        return
    
    print(f'{format.upper()} file has been saved to {output_file_path}')

# Example usage:
generate_pnm(filename='color_gradient', format='ppm', width=256, height=256)
generate_pnm(filename='gray_gradient', format='pgm', width=256, height=256)
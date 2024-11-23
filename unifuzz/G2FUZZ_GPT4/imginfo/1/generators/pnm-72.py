import os

def create_checkerboard(width, height, cell_size):
    """Generate a checkerboard pattern for PBM."""
    rows = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append((x // cell_size + y // cell_size) % 2)
        rows.append(' '.join(str(cell) for cell in row))
    return "\n".join(rows)

def create_gradient(width, height):
    """Generate a red to green gradient for PPM."""
    rows = []
    max_color_value = 255
    for y in range(height):
        row = []
        for x in range(width):
            red_value = int((x / width) * max_color_value)
            green_value = max_color_value - red_value
            blue_value = 0 # Keeping blue constant for simplicity
            row.append(f"{red_value} {green_value} {blue_value}")
        rows.append(' '.join(row))
    return "\n".join(rows)

def generate_pnm_files():
    os.makedirs('./tmp/', exist_ok=True)
    
    # Checkerboard PBM
    pbm_width, pbm_height, pbm_cell_size = 8, 8, 2
    pbm_data = f"""P1
# Checkerboard PBM example
{pbm_width} {pbm_height}
{create_checkerboard(pbm_width, pbm_height, pbm_cell_size)}
"""
    with open('./tmp/checkerboard.pbm', 'w') as f:
        f.write(pbm_data)
    
    # Gradient PPM
    ppm_width, ppm_height = 256, 50
    ppm_data = f"""P3
# Gradient PPM example
{ppm_width} {ppm_height}
255
{create_gradient(ppm_width, ppm_height)}
"""
    with open('./tmp/gradient.ppm', 'w') as f:
        f.write(ppm_data)
    
    print("Complex PNM files have been generated and saved in './tmp/'.")

# Execute the function to generate PNM files
generate_pnm_files()
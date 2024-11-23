import os

def save_pnm_file(filename, width, height, max_val, data):
    with open(filename, 'w') as f:
        f.write(f'P3\n{width} {height}\n{max_val}\n')
        for row in data:
            f.write(' '.join(row) + '\n')

def generate_pnm_file(filename, width, height, max_val):
    data = [['255', '0', '0'] * width for _ in range(height)]  # Red color image
    save_pnm_file(filename, width, height, max_val, data)

# Create tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate and save pnm files with specified features
generate_pnm_file('./tmp/red_image.pnm', 100, 100, 255)
generate_pnm_file('./tmp/green_image.pnm', 150, 150, 255)
generate_pnm_file('./tmp/blue_image.pnm', 200, 200, 255)
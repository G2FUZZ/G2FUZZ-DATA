import os

def generate_pnm_file(file_name, format='P3'):
    # Create a sample PNM content
    content = f"{format}\n# Generated PNM file\n5 5\n255\n"
    for i in range(25):
        content += f"{i} {i} {i}\n"

    # Save the content to a file
    file_path = f"./tmp/{file_name}.pnm"
    with open(file_path, 'w') as file:
        file.write(content)

# Create the ./tmp/ directory if it doesn't exist
os.makedirs('./tmp', exist_ok=True)

# Generate ASCII PNM file
generate_pnm_file('ascii_pnm', format='P3')

# Generate Binary PNM file
generate_pnm_file('binary_pnm', format='P6')
import os

# Function to generate PNM file with specified content
def generate_pnm_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Create directory for saving PNM files
os.makedirs('./tmp/', exist_ok=True)

# Generate PNM file with specified content
pnm_content = "P1\n# Generated PNM file\n1 1\n0"
generate_pnm_file('./tmp/no_color_profiles.pnm', pnm_content)
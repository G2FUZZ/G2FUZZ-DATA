import os

# Function to generate PNM file with specified content
def generate_pnm_file(filename, header, data):
    with open(filename, 'w') as file:
        file.write(header)
        file.write('\n')
        for row in data:
            file.write(' '.join(row))
            file.write('\n')

# Create directory for saving PNM files
os.makedirs('./tmp/', exist_ok=True)

# Generate PNM file with specified content
pnm_header = "P3\n# Generated PNM file\n5 5\n255"
pnm_data = [
    ['255', '0', '0'], ['0', '255', '0'], ['0', '0', '255'], ['255', '255', '0'], ['255', '0', '255'],
    ['0', '255', '255'], ['128', '0', '0'], ['0', '128', '0'], ['0', '0', '128'], ['128', '128', '0'],
    ['128', '0', '128'], ['0', '128', '128'], ['192', '192', '192'], ['128', '128', '128'], ['64', '64', '64'],
    ['255', '255', '255']
]
generate_pnm_file('./tmp/multi_channel_image.pnm', pnm_header, pnm_data)
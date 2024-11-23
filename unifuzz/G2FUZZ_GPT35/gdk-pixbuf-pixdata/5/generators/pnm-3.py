import os

def create_pnm_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Creating PNM file with uncompressed image data
image_data = "P3\n# This is a PNM file\n3 2\n255\n255 0 0 0 255 0 0 0 255\n"
create_pnm_file('./tmp/compressed_image.pnm', image_data)

print("PNM files with uncompressed image data have been created and saved in './tmp/' directory.")
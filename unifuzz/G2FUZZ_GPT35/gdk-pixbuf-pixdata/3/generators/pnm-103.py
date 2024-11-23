import os

def generate_complex_pnm_file(file_name, header, image_data):
    with open(file_name, 'w') as file:
        file.write(header)
        file.write('\n')
        for layer in image_data:
            for row in layer:
                file.write(' '.join(row))
                file.write('\n')

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

header = "P3\n# This is a complex PNM file with multiple layers\n10 10\n255"
layer1 = [
    ['255', '0', '0'] * 10,
    ['0', '255', '0'] * 10,
    ['0', '0', '255'] * 10
]
layer2 = [
    ['0', '0', '255'] * 10,
    ['255', '0', '0'] * 10,
    ['0', '255', '0'] * 10
]
image_data = [layer1, layer2]

file_name = './tmp/complex_generated_file.pnm'
generate_complex_pnm_file(file_name, header, image_data)

print(f"Generated complex 'pnm' file saved at: {file_name}")
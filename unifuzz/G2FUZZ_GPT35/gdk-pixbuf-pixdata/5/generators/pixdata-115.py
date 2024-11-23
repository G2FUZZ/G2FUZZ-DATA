import os

# Create a directory to store the pixdata files
os.makedirs('./tmp/', exist_ok=True)

# Generate the pixdata files with additional color attribute
layer_info = {
    'layer1': {
        'name': 'Background',
        'type': 'Image',
        'size': (1920, 1080),
        'color': 'Blue'
    },
    'layer2': {
        'name': 'Text Overlay',
        'type': 'Text',
        'font': 'Arial',
        'size': (400, 100),
        'color': 'Red'
    },
    'layer3': {
        'name': 'Logo',
        'type': 'Image',
        'size': (200, 200),
        'color': 'Green'
    }
}

for layer_name, info in layer_info.items():
    filename = f'./tmp/{layer_name}_pixdata.txt'
    with open(filename, 'w') as file:
        file.write(f'Layer Name: {info["name"]}\n')
        file.write(f'Layer Type: {info["type"]}\n')
        if 'font' in info:
            file.write(f'Font: {info["font"]}\n')
        file.write(f'Size: {info["size"][0]}x{info["size"][1]}\n')
        file.write(f'Color: {info["color"]}\n')

print("pixdata files with additional color attribute have been generated and saved in ./tmp/")
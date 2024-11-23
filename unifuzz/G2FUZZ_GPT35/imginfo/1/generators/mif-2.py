import os

# Create a directory to store the generated files
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate mif files with specified page layout features
page_layouts = [
    {"page_dimensions": "A4", "margins": "1 inch", "orientation": "landscape"},
    {"page_dimensions": "Letter", "margins": "0.5 inch", "orientation": "portrait"},
    {"page_dimensions": "Legal", "margins": "1.5 inch", "orientation": "landscape"}
]

for idx, layout in enumerate(page_layouts):
    filename = os.path.join(directory, f'page_layout_{idx + 1}.mif')
    with open(filename, 'w') as file:
        file.write(f"Page Dimensions: {layout['page_dimensions']}\n")
        file.write(f"Margins: {layout['margins']}\n")
        file.write(f"Orientation: {layout['orientation']}\n")

    print(f"Generated {filename}")

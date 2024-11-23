from PIL import Image
import tifffile as tiff

# Create a multi-layer tiff file with metadata
data = {
    'layer1': Image.new('RGB', (100, 100), color='green'),
    'layer2': Image.new('RGB', (100, 100), color='blue'),
}

with tiff.TiffWriter('./tmp/multi_layer_image.tif') as tif:
    for name, img in data.items():
        img_array = img.resize((100, 100)).convert('L').convert('RGB')  # Convert to RGB for saving
        tif.save(img_array, description=f'Layer: {name}')

    tif.imagej_metadata = {
        'Info': 'This is a multi-layer TIFF file with metadata',
        'Author': 'John Doe',
        'Date': '2022-01-01'
    }
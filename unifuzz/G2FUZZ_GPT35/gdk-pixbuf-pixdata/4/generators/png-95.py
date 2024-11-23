from PIL import Image
from PIL.PngImagePlugin import PngInfo

# Create a new PNG image with a transparent background
image = Image.new('RGBA', (200, 200), color=(255, 255, 255, 0))

# Add metadata to the image
metadata = PngInfo()
metadata.add_text('Author', 'Jane Smith')
metadata.add_text('Title', 'Landscape Artwork')
metadata.add_text('Description', 'A beautiful landscape painting')

# Create a new chunk with custom data
custom_chunk_data = b'CustomData123'
custom_chunk = b'tEXt' + custom_chunk_data
image.info['custom_chunk'] = custom_chunk

# Add a custom zTXt chunk for compressed text data
ztxt_chunk_data = b'CompressedTextData456789'
ztxt_chunk = b'zTXt' + ztxt_chunk_data
image.info['ztxt_chunk'] = ztxt_chunk

# Save the image with metadata and custom chunks
image.save('./tmp/complex_metadata_example.png', pnginfo=metadata)
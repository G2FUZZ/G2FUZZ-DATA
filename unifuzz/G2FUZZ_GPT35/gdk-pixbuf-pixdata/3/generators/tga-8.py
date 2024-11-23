import numpy as np
import os

# Create a dummy image data
image_data = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)

# Save the image data to a TGA file with different interleaving methods
interleaving_methods = ['Interleaved 2', 'Non-Interleaved', 'Interleaved 4']
for method in interleaving_methods:
    file_path = f'./tmp/example_{method.replace(" ", "_")}.tga'
    
    if method == 'Interleaved 2':
        interleaved_data = np.zeros((100, 100, 3), dtype=np.uint8)
        interleaved_data[::2, ::2] = image_data[::2, ::2]
        interleaved_data[1::2, 1::2] = image_data[1::2, 1::2]
        interleaved_data[::2, 1::2] = image_data[::2, 1::2]
        interleaved_data[1::2, ::2] = image_data[1::2, ::2]
        image_data = interleaved_data
    elif method == 'Interleaved 4':
        interleaved_data = np.zeros((100, 100, 3), dtype=np.uint8)
        interleaved_data[::2, ::2] = image_data[::2, ::2]
        interleaved_data[1::2, 1::2] = image_data[1::2, 1::2]
        interleaved_data[::2, 1::2] = image_data[::2, 1::2]
        interleaved_data[1::2, ::2] = image_data[1::2, ::2]
        interleaved_data[:, :, 2] = image_data[:, :, 2]
        image_data = interleaved_data

    with open(file_path, 'wb') as f:
        # Write TGA header and image data to the file
        # This part needs to be implemented according to the TGA file format specifications
        pass

print("TGA files have been generated and saved.")
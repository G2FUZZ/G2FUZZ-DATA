import numpy as np

# Create a sample image data
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Write the image data to a TGA file
with open('./tmp/sample_image.tga', 'wb') as f:
    # Write the TGA header (not fully compliant, just for demonstration)
    f.write(bytes([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100 % 256, 100 // 256, 100 % 256, 100 // 256, 24, 0]))
    
    # Write the image data in BGR format
    f.write(image_data[:,:,2].tobytes())
    f.write(image_data[:,:,1].tobytes())
    f.write(image_data[:,:,0].tobytes())
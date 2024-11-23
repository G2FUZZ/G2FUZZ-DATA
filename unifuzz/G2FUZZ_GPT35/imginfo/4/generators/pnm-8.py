import numpy as np

# Create a simple example image data
image_data = np.array([[0, 255, 0], [255, 0, 255], [0, 255, 0]], dtype=np.uint8)

# Save the image data as a PGM file (Portable Gray Map)
with open('./tmp/lossless_image.pgm', 'wb') as file:
    file.write(b'P2\n')
    file.write(b'# Lossless image\n')
    file.write(b'3 3\n')
    file.write(b'255\n')
    np.savetxt(file, image_data, fmt='%d')

# Save the image data as a PBM file (Portable Bit Map)
binary_image_data = (image_data > 127).astype(np.uint8)
with open('./tmp/lossless_binary_image.pbm', 'wb') as file:
    file.write(b'P1\n')
    file.write(b'# Lossless binary image\n')
    file.write(b'3 3\n')
    np.savetxt(file, binary_image_data, fmt='%d', delimiter=' ', newline='\n')
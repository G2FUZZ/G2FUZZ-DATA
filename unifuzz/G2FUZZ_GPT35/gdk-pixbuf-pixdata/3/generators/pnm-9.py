import numpy as np

# Define the text to be saved in the pnm file
text = "9. Widely Supported: The 'pnm' format is supported by many image processing tools and libraries, making it a common choice for simple image storage and manipulation."

# Create a numpy array with the ASCII values of the characters in the text
data = np.array([ord(char) for char in text])

# Define the file path
file_path = './tmp/generated_file.pnm'

# Save the data to a pnm file
with open(file_path, 'wb') as file:
    file.write(bytearray([0x50, 0x35, 0x0A]))  # P5 followed by newline
    file.write(bytearray(f"{len(text)} {1}\n".encode()))  # Width is the length of text, height is 1
    file.write(bytearray("255\n".encode()))  # Maximum gray value
    file.write(data.astype(np.uint8).tobytes())
import numpy as np

# Define the text to be saved in the pnm file
text = "Complex PNM File Structure Example"

# Create a numpy array with the ASCII values of the characters in the text
data = np.array([ord(char) for char in text])

# Define the file path
file_path = './tmp/complex_generated_file.pnm'

# Save the data to a pnm file with a more complex structure
with open(file_path, 'wb') as file:
    file.write(bytearray([0x50, 0x36, 0x0A]))  # P6 followed by newline
    file.write(bytearray(f"8 4\n".encode()))  # Width is 8, height is 4
    file.write(bytearray("255\n".encode()))  # Maximum gray value

    # Generate multiple rows of data with varying gray values
    for i in range(4):
        row_data = data * (i + 1)  # Varying gray values based on row index
        file.write(row_data.astype(np.uint8).tobytes())
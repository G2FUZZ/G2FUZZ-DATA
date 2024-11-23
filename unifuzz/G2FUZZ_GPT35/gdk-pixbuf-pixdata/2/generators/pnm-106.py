import numpy as np

def create_complex_pnm(width, height, max_val, data, comments=None):
    encoded_data = bytearray()
    
    # Adding comments to the PNM file
    if comments:
        for comment in comments:
            encoded_data += f"# {comment}\n".encode()
    
    # Convert data to grayscale or RGB if the number of components is not 1 or 3
    num_components = data.shape[-1]
    if num_components == 1:
        encoded_data += f"P5\n{width} {height}\n{max_val}\n".encode()  # Grayscale PGM
        data = data.reshape((height, width))  # Convert to 2D grayscale data
    elif num_components == 3:
        encoded_data += f"P6\n{width} {height}\n{max_val}\n".encode()  # RGB PPM
    else:
        # Convert to grayscale if number of components is not supported
        encoded_data += f"P5\n{width} {height}\n{max_val}\n".encode()  # Grayscale PGM
        data = np.mean(data, axis=-1, keepdims=True).astype(np.uint8)  # Convert to grayscale
    
    # Encoding image pixel data
    if data.dtype == np.uint8:
        encoded_data += data.tobytes()
    else:
        encoded_data += data.astype(np.uint8).tobytes()
    
    return encoded_data

def save_pnm_file(file_path, encoded_data):
    with open(file_path, 'wb') as file:
        file.write(encoded_data)

# Sample data parameters
width = 100
height = 100
max_val = 255

# Creating sample data with comments
comments = ["Sample PNM file with comments", "Created by YourName"]
complex_data = np.random.randint(0, max_val + 1, (height, width, 4))  # Random RGBA data for complex PNM

# Saving a complex PNM file with comments
save_pnm_file('./tmp/sample_complex.pnm', create_complex_pnm(width, height, max_val, complex_data, comments))
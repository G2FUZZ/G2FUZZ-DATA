import os
import random

def generate_data():
    """Generate random data to simulate file content."""
    return [random.randint(0, 255) for _ in range(10)]

def calculate_checksum(data):
    """Calculate a simple checksum by summing all the data bytes."""
    return sum(data) % 256

def calculate_parity(data):
    """Calculate a simple parity (even) for minimal error correction."""
    parity = 0
    for byte in data:
        parity ^= byte
    return parity

def write_pixdata_file(file_path, data, checksum, parity):
    """Write the data, checksum, and parity to a file."""
    with open(file_path, 'w') as file:
        file_content = ' '.join(map(str, data)) + '\n'
        file_content += f"Checksum: {checksum}\n"
        file_content += f"Parity: {parity}\n"
        file.write(file_content)

def main():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Generate data
    data = generate_data()
    
    # Calculate checksum and parity
    checksum = calculate_checksum(data)
    parity = calculate_parity(data)
    
    # File path
    file_path = './tmp/pixdata_1.txt'
    
    # Write to file
    write_pixdata_file(file_path, data, checksum, parity)
    
    print(f"File {file_path} has been created with data, checksum, and parity.")

if __name__ == "__main__":
    main()
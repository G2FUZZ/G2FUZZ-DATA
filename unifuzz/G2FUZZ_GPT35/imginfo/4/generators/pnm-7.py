import os

def generate_pnm_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

content = "Portability: Can be easily transferred between different platforms and software applications"
filename = './tmp/example.pnm'

generate_pnm_file(content, filename)

print(f"Created pnm file: {filename}")
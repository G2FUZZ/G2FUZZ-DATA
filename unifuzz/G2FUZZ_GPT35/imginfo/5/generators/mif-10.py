import os

# Create a directory for storing the generated files
os.makedirs('./tmp/', exist_ok=True)

num_files = 5

for i in range(num_files):
    filename = f'file_{i}.mif'
    with open(f'./tmp/{filename}', 'w') as f:
        f.write(f'Indexing information for {filename}\n')
        
print(f'{num_files} mif files generated and saved in ./tmp/ directory.')
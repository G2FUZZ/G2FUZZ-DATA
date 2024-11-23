import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Define the custom data structure for the pixdata files with more complex features
pixdata = {
    'file1': {
        'feature1': 'Custom data structures',
        'feature2': 'Some files may include custom data structures for specific applications or purposes.',
        'metadata': {
            'author': 'John Doe',
            'created_at': '2022-01-01'
        }
    },
    'file2': {
        'feature1': 'Custom classes',
        'feature2': 'Files may contain custom classes to represent complex data structures.',
        'nested_structure': {
            'sub_feature1': 'Nested data',
            'sub_feature2': 'Supports hierarchical data representation'
        }
    }
}

# Save the pixdata into separate files in the './tmp/' directory
for file_name, data in pixdata.items():
    with open(f'./tmp/{file_name}.txt', 'w') as f:
        f.write(f"Feature 1: {data['feature1']}\n")
        f.write(f"Feature 2: {data['feature2']}\n")
        
        if 'metadata' in data:
            f.write(f"Metadata:\n")
            for key, value in data['metadata'].items():
                f.write(f"  {key}: {value}\n")
        
        if 'nested_structure' in data:
            f.write(f"Nested Structure:\n")
            for key, value in data['nested_structure'].items():
                f.write(f"  {key}: {value}\n")

print("Generated pixdata files with complex features saved in './tmp/' directory.")
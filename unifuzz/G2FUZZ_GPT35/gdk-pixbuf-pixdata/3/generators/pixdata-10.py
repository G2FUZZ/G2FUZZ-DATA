import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Define the custom data structure for the pixdata files
pixdata = {
    'file1': {
        'feature1': 'Custom data structures',
        'feature2': 'Some files may include custom data structures for specific applications or purposes.'
    },
    'file2': {
        'feature1': 'Custom classes',
        'feature2': 'Files may contain custom classes to represent complex data structures.'
    }
}

# Save the pixdata into separate files in the './tmp/' directory
for file_name, data in pixdata.items():
    with open(f'./tmp/{file_name}.txt', 'w') as f:
        f.write(f"Feature 1: {data['feature1']}\n")
        f.write(f"Feature 2: {data['feature2']}\n")

print("Generated pixdata files saved in './tmp/' directory.")
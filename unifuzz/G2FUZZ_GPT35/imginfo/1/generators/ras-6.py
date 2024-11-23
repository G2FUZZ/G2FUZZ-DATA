import os

# Define the features
features = """
1. File Name: sample_file1.ras
2. File Size: 1024 bytes
3. Creation Date: 2022-09-01
4. Creator: User1
5. Content: This is a sample ras file.
"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate and save the 'ras' files
for i in range(3):
    file_name = f'./tmp/sample_file{i+1}.ras'
    with open(file_name, 'w') as file:
        file.write(features)
        print(f'{file_name} generated successfully!')
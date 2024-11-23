import os

# Define the features to be written to the 'ras' files
features = "9. Compatibility: 'ras' files may be less common compared to other image formats like JPEG or PNG, impacting their compatibility with different software applications."

# Create a directory if it doesn't exist to store the 'ras' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ras' files with the specified features
for i in range(3):
    filename = f'./tmp/file{i + 1}.ras'
    with open(filename, 'w') as file:
        file.write(features)

print("Generated 'ras' files successfully.")
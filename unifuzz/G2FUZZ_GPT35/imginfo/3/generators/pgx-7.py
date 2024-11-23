import os

# Create a directory to store the 'pgx' files
directory = './tmp'
os.makedirs(directory, exist_ok=True)

# Generate 'pgx' files with the specified feature
feature = "Customization: Progenex software allows users to customize the data stored in 'pgx' files based on their specific research needs."

for i in range(3):  # Generate 3 'pgx' files
    filename = f'{directory}/file_{i + 1}.pgx'
    with open(filename, 'w') as file:
        file.write(feature)

print("Generated 'pgx' files successfully in the './tmp/' directory.")
import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the features for the pixdata files
features = "Encryption: Security features like encryption may be used to protect the data in the file."

# Generate and save the pixdata files
for i in range(1, 4):
    file_name = f'pixdata_{i}.txt'
    with open(os.path.join(directory, file_name), 'w') as file:
        file.write(features)

print("Generated pixdata files successfully.")
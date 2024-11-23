import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate the 'pixdata' files with the specified feature
for i in range(3):
    filename = f'./tmp/pixdata_{i}.pixdata'
    with open(filename, 'w') as file:
        file.write('This is a pixdata file with some data.')

print("Files generated successfully.")
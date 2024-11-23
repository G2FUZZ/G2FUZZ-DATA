import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pgx files with the specified features
for i in range(1, 4):
    with open(f'./tmp/file{i}.pgx', 'w') as file:
        file.write("Progressive Loading: 'pgx' files can be structured to allow for progressive loading, where lower-resolution versions of the image are displayed first, followed by higher resolutions for better user experience.")
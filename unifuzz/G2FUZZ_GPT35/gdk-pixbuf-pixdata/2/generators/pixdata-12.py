import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pixdata files with the specified feature
feature = "Color profile: Can include color profiles for accurate color representation across different devices."
for i in range(3):
    with open(f'./tmp/pixdata{i}.txt', 'w') as f:
        f.write(feature)

print("pixdata files generated successfully!")
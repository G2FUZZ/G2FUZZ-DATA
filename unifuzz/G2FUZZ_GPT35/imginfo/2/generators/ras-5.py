import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate the content for the ras files
ras_content = "Transparency: Supports transparency through an alpha channel in 32-bit RAS files."

# Save the generated content into ras files
for i in range(3):
    with open(f'./tmp/file_{i}.ras', 'w') as file:
        file.write(ras_content)

print("RAS files generated successfully.")
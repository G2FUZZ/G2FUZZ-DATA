import os

# Create a directory to save the 'ras' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ras' files with the specified feature
feature = "7. Platform Independence: 'ras' files are platform-independent and can be read on different operating systems."
for i in range(3):
    with open(f'./tmp/file_{i+1}.ras', 'w') as file:
        file.write(feature)

print("Generated 'ras' files successfully.")
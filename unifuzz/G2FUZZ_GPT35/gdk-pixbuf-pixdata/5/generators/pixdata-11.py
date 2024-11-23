import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with the specified feature
pixdata = "11. Alpha channel: Additional channel for transparency information in images."

with open('./tmp/pixdata1.txt', 'w') as file:
    file.write(pixdata)

with open('./tmp/pixdata2.txt', 'w') as file:
    file.write(pixdata)

print("pixdata files generated and saved successfully!")
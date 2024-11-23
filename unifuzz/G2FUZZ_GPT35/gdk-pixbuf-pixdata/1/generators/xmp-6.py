import os

# Define the content of the xmp file
content = """
6. Standardization: XMP is an ISO standard (ISO 16684-1), ensuring compatibility and interoperability across different software applications.
"""

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the content to a new xmp file
with open('./tmp/standardization.xmp', 'w') as file:
    file.write(content)

print("XMP file has been generated and saved successfully.")
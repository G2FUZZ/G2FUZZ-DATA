import os

# Define the content to be included in the XMP file
xmp_content = """
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:xmp="http://ns.adobe.com/xap/1.0/">
    <rdf:Description rdf:about=""
        xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:description>Interoperability: XMP provides a standard format for the creation, processing, and interchange of standardized and custom metadata for digital documents and data sets. XMP is designed to work across different platforms, supporting a wide range of file formats including PDF, JPEG, GIF, PNG, TIFF, MP3, and many others.</dc:description>
    </rdf:Description>
</rdf:RDF>
"""

# Directory to save the XMP file
directory = './tmp/'

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the file path
file_path = os.path.join(directory, 'features.xmp')

# Write the content to the XMP file
with open(file_path, 'w') as file:
    file.write(xmp_content.strip())

print(f'XMP file saved to {file_path}')
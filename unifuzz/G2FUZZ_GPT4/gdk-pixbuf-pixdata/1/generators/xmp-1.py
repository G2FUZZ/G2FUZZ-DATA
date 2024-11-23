import os

# Create the ./tmp/ directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# XMP content to be written to the file
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>Standardization: XMP provides a standard format for the creation, processing, and interchange of standardized and custom metadata for digital documents and data sets. It is designed to work across different platforms, making it versatile for various applications.</dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Path where the XMP file will be saved
file_path = './tmp/example.xmp'

# Writing the XMP content to the file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file has been successfully created at {file_path}')
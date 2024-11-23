import os

# Define the XMP content with the features described
xmp_content = """
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP toolkit">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>3. **Embeddable**: XMP data can be embedded into a wide range of digital file formats without altering the original content. This includes popular formats like JPEG, TIFF, PDF, and many raw image formats. Embedding metadata directly into files ensures that the information travels with the file, enhancing portability and accessibility.</dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
"""

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the path for the new XMP file
xmp_file_path = './tmp/features.xmp'

# Write the XMP content to the file
with open(xmp_file_path, 'w') as file:
    file.write(xmp_content.strip())

print(f'XMP file saved at {xmp_file_path}')
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content to be included in the XMP file
xmp_content = """
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
        xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    4. **Embeddable**: XMP can be embedded into a wide range of digital file formats without affecting their primary function. This includes popular formats like JPEG, TIFF, PDF, and many Adobe-specific formats such as PSD and AI.
   </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
""".strip()

# Define the path to the XMP file
file_path = './tmp/example.xmp'

# Write the content to the XMP file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file created at {file_path}')
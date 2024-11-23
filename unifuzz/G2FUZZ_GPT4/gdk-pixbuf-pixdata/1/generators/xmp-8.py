import os

# Define the XMP content
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    8. **Integration with Adobe Products**: As an Adobe-developed standard, XMP is tightly integrated with Adobe's suite of products, 
    allowing for seamless metadata handling across Adobe applications like Photoshop, Lightroom, and Acrobat.
   </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the file path
file_path = './tmp/example.xmp'

# Write the XMP content to the file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file has been created at {file_path}')
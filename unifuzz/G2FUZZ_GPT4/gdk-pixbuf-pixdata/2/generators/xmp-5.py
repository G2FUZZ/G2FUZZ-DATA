import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the XMP file
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    Synchronization of Metadata: XMP facilitates the synchronization of metadata among different files, ensuring consistency across documents, images, and other media types. If embedded metadata is edited in one file, it can be updated across related files.
   </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
'''

# Define the file path
file_path = './tmp/feature_description.xmp'

# Write the content to the XMP file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file generated at: {file_path}")
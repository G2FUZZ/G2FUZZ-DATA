import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP content with the feature description
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    7. **Synchronization**: XMP allows for the synchronization of metadata across different copies of a file, ensuring consistency and accuracy of information across digital assets.
   </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Path to the XMP file to be created
xmp_file_path = './tmp/feature_description.xmp'

# Write the XMP content to the file
with open(xmp_file_path, 'w') as xmp_file:
    xmp_file.write(xmp_content)

print(f"XMP file created at {xmp_file_path}")
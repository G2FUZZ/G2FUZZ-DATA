import os

# Define the directory and file name
directory = './tmp/'
file_name = 'metadata_sync.xmp'
full_path = os.path.join(directory, file_name)

# XMP content with the features description
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    7. **Synchronization of Metadata**: XMP supports the synchronization of metadata across different file formats. For instance, changes made to the metadata in one file can be automatically applied to related
    files, ensuring consistency across documents and media types.
   </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Write the XMP content to the file
with open(full_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file created at {full_path}")
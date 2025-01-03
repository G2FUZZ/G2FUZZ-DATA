import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP content
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    dc:title="Searchability and Organization"
    dc:description="By providing standardized, structured metadata, XMP enhances the searchability and organization of digital assets. This makes it easier to find, sort, and manage files based on various criteria such as author, creation date, location, and more.">
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# File path where the XMP will be saved
file_path = './tmp/feature_metadata.xmp'

# Writing the XMP content to the file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file saved at: {file_path}")
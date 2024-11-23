import os

# Define the directory and file name
directory = './tmp/'
file_name = 'features.xmp'

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Content to be written in the XMP file
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    dc:title="Extensibility"
    dc:description="XMP is designed to be extensible, meaning it can support existing metadata standards as well as allow the creation of custom metadata fields. This flexibility ensures that XMP can be adapted to specific needs and uses, including those that may arise in the future.">
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Full path for the file
full_path = os.path.join(directory, file_name)

# Write the content to the XMP file
with open(full_path, 'w') as file:
    file.write(xmp_content)

print(f"'{file_name}' has been successfully created in '{directory}'.")
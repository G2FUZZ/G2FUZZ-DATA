import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# XMP content to be written to the file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    5. **Read and Write Support**: Many software applications can read and write XMP metadata, from professional photo and video editing tools to consumer-grade media managers. This widespread support ensures that XMP metadata is widely accessible and usable.
   </dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# File path for the new XMP file
xmp_file_path = './tmp/features.xmp'

# Writing the XMP content to the file
with open(xmp_file_path, 'w', encoding='utf-8') as file:
    file.write(xmp_content)

print(f'XMP file saved to {xmp_file_path}')
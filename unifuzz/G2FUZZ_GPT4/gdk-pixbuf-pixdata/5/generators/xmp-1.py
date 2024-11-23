import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the XMP file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:format>application/pdf</dc:format>
   <dc:format>image/jpeg</dc:format>
   <dc:format>image/jp2</dc:format>
   <dc:format>image/gif</dc:format>
   <dc:format>image/png</dc:format>
   <dc:format>image/tiff</dc:format>
   <dc:format>text/html</dc:format>
   <dc:format>text/plain</dc:format>
   <dc:format>audio/mpeg</dc:format>
   <dc:format>video/mp4</dc:format>
   <dc:description>Embedded Metadata: Unlike many other metadata formats that store information in separate files, XMP can embed metadata directly into the file it describes, supporting a wide range of file types.</dc:description>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Path where the XMP file will be saved
xmp_file_path = './tmp/embedded_metadata.xmp'

# Writing the XMP content to the file
with open(xmp_file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file saved to {xmp_file_path}")
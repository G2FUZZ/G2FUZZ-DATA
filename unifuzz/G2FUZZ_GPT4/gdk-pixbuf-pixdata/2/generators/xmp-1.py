import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the path for the new XMP file
xmp_file_path = './tmp/metadata.xmp'

# Define the XMP content with metadata embedding description
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c015 81.159824, 2016/09/10-02:41:30        ">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/">
         <dc:format>application/pdf</dc:format>
         <dc:title>
            <rdf:Alt>
               <rdf:li xml:lang="x-default">Metadata Embedding Example</rdf:li>
            </rdf:Alt>
         </dc:title>
         <dc:description>
            <rdf:Alt>
               <rdf:li xml:lang="x-default">XMP allows for the embedding of metadata directly into files of various formats without altering the original content. This ensures that the information about the file travels with the file itself, across platforms and applications.</rdf:li>
            </rdf:Alt>
         </dc:description>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Write the XMP content to the file
with open(xmp_file_path, 'w') as xmp_file:
    xmp_file.write(xmp_content)

print(f'XMP file created at {xmp_file_path}')
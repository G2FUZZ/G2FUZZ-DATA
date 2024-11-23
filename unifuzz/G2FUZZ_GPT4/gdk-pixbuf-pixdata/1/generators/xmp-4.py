import os

# Define the XMP content
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
        xmlns:xmp="http://ns.adobe.com/xap/1.0/">
   <xmp:Interoperability>XMP facilitates interoperability between different applications, systems, and platforms. Metadata created in one application can be read and modified in another, supporting a seamless workflow across different software tools.</xmp:Interoperability>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Save the XMP content to a file
file_path = './tmp/feature.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'File saved to {file_path}')
import os

# Create a directory to store the XMP files
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP files with the given feature
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/">
         <xmp:ModifyDate>2022-10-10T12:00:00</xmp:ModifyDate>
         <dc:format>image/jpeg</dc:format>
         <dc:description>
            <rdf:Alt>
               <rdf:li xml:lang="x-default">XMP metadata can be embedded within various file formats like images, videos, and PDFs.</rdf:li>
            </rdf:Alt>
         </dc:description>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Save the XMP file to ./tmp/ directory
with open('./tmp/example.xmp', 'w') as f:
    f.write(xmp_content)
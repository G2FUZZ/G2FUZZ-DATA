import os

# Define the XMP template
xmp_template = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP toolkit">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
           xmlns:ns1="http://example.com/ns#">
    <rdf:Description rdf:about=""
                     xmlns:xmp="http://ns.adobe.com/xap/1.0/"
                     ns1:Granularity="Metadata can be attached not just to the file as a whole, but also to specific parts of the file, such as a particular image in a document or a specific frame in a video, allowing for detailed descriptions of complex digital assets.">
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the filename
filename = './tmp/granularity_feature.xmp'

# Write the XMP data to a file
with open(filename, 'w') as file:
    file.write(xmp_template)

print(f'XMP file saved to {filename}')
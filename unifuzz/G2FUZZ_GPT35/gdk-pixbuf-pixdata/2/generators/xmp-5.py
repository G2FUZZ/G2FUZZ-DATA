import os

# Define the content for the XMP file
xmp_content = """
<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about=''
            xmlns:xmp='http://ns.adobe.com/xap/1.0/'>
            <xmp:Versioning>XMP supports versioning of metadata, enabling tracking of changes and revisions to the metadata over time.</xmp:Versioning>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Write the XMP content to a file
with open('./tmp/example.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file generated successfully!")
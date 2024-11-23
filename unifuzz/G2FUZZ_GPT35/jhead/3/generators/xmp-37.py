import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP file with more complex file structures
xmp_content = """
<?xpacket begin='﻿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about=''
            xmlns:xmp='http://ns.adobe.com/xap/1.0/'>
            <xmp:ModifyDate>2022-01-01T12:00:00</xmp:ModifyDate>
            <xmp:MetadataDate>2022-01-01T12:00:00</xmp:MetadataDate>
            <xmp:CreatorTool>Python XMP Generator</xmp:CreatorTool>
            <xmp:Version>1.0</xmp:Version>
            <rdf:Bag>
                <rdf:li>Tag1</rdf:li>
                <rdf:li>Tag2</rdf:li>
            </rdf:Bag>
        </rdf:Description>
        <rdf:Description rdf:about='image.jpg'
            xmlns:dc='http://purl.org/dc/elements/1.1/'>
            <dc:format>image/jpeg</dc:format>
            <dc:creator>John Doe</dc:creator>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

# Save the XMP file
file_path = os.path.join(directory, 'metadata_complex.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file with more complex file structures saved at: {file_path}")
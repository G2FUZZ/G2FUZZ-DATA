import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the XMP file with more complex structures
xmp_content = """<?xpacket begin='﻿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about='' xmlns:dc='http://purl.org/dc/elements/1.1/'>
            <dc:title>XMP File Title</dc:title>
            <dc:creator>XMP File Creator</dc:creator>
            <dc:description>XMP File Description</dc:description>
            <dc:date>2022-01-01</dc:date>
            <dc:format>application/pdf</dc:format>
            <dc:language>en-US</dc:language>
            <dc:publisher>XMP File Publisher</dc:publisher>
            <dc:subject>XMP File Subject</dc:subject>
            <dc:identifier>XMP-123456</dc:identifier>
            <dc:type>Text</dc:type>
            <dc:source>XMP File Source</dc:source>
            <dc:relation>XMP File Relation</dc:relation>
            <dc:coverage>XMP File Coverage</dc:coverage>
            <dc:contributor>XMP File Contributor</dc:contributor>
            <dc:format>application/pdf</dc:format>
        </rdf:Description>
        <rdf:Description rdf:about='http://www.example.com/' xmlns:ex='http://www.example.com/ns/'>
            <ex:customProperty>Custom Value</ex:customProperty>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

# Save the XMP file with more complex structures
with open('./tmp/extended_xmp_file.xmp', 'w') as file:
    file.write(xmp_content)

print("Extended version of XMP file with complex structures has been generated and saved.")
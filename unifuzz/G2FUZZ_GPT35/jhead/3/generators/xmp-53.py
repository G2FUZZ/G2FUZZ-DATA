import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the extended XMP file with even more complex structures
xmp_content_extended = """<?xpacket begin='﻿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about='' xmlns:dc='http://purl.org/dc/elements/1.1/'>
            <dc:title>XMP Extended File Title</dc:title>
            <dc:creator>XMP Extended File Creator</dc:creator>
            <dc:description>XMP Extended File Description</dc:description>
            <dc:date>2022-01-01</dc:date>
            <dc:format>application/pdf</dc:format>
            <dc:language>en-US</dc:language>
            <dc:publisher>XMP Extended File Publisher</dc:publisher>
            <dc:subject>XMP Extended File Subject</dc:subject>
            <dc:identifier>XMP-789012</dc:identifier>
            <dc:type>Text</dc:type>
            <dc:source>XMP Extended File Source</dc:source>
            <dc:relation>XMP Extended File Relation</dc:relation>
            <dc:coverage>XMP Extended File Coverage</dc:coverage>
            <dc:contributor>XMP Extended File Contributor</dc:contributor>
            <dc:format>application/pdf</dc:format>
            <dc:rights>XMP Extended File Rights</dc:rights>
            <dc:alternative>XMP Extended File Alternative</dc:alternative>
            <dc:temporal>XMP Extended File Temporal</dc:temporal>
            <dc:customProperty>
                <rdf:Bag>
                    <rdf:li>Custom Value 1</rdf:li>
                    <rdf:li>Custom Value 2</rdf:li>
                </rdf:Bag>
            </dc:customProperty>
            <dc:extensionProperty>
                <ex:extendedProperty1>Extended Value 1</ex:extendedProperty1>
                <ex:extendedProperty2>Extended Value 2</ex:extendedProperty2>
            </dc:extensionProperty>
            <dc:complexProperty>
                <ex:complexValue>
                    <rdf:Description>
                        <ex:subProperty1>Sub Value 1</ex:subProperty1>
                        <ex:subProperty2>Sub Value 2</ex:subProperty2>
                    </rdf:Description>
                </ex:complexValue>
            </dc:complexProperty>
        </rdf:Description>
        <rdf:Description rdf:about='http://www.example.com/' xmlns:ex='http://www.example.com/ns/'>
            <ex:customProperty>Custom Value</ex:customProperty>
            <ex:additionalProperty>
                <rdf:Description>
                    <ex:subProperty1>Sub Value 1</ex:subProperty1>
                    <ex:subProperty2>Sub Value 2</ex:subProperty2>
                </rdf:Description>
            </ex:additionalProperty>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

# Save the extended XMP file with even more complex structures
with open('./tmp/extended_xmp_file_extended.xmp', 'w') as file:
    file.write(xmp_content_extended)

print("Extended version of XMP file with even more complex structures has been generated and saved.")
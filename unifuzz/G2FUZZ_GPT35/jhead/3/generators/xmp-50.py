import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the extended XMP file with even more complex structures
xmp_content_extended = """<?xpacket begin='﻿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#' xmlns:ex='http://www.example.com/ns/' xmlns:custom='http://www.custom.com/ns/'>
        <rdf:Description rdf:about='' xmlns:dc='http://purl.org/dc/elements/1.1/'>
            <dc:title>XMP Extended File Title</dc:title>
            <dc:creator>
                <rdf:Seq>
                    <rdf:li>XMP Extended Creator 1</rdf:li>
                    <rdf:li>XMP Extended Creator 2</rdf:li>
                </rdf:Seq>
            </dc:creator>
            <dc:subject>
                <rdf:Alt>
                    <rdf:li xml:lang='en'>Subject 1 in English</rdf:li>
                    <rdf:li xml:lang='fr'>Sujet 1 en français</rdf:li>
                </rdf:Alt>
            </dc:subject>
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
            <custom:additionalProperty>
                <rdf:Description>
                    <custom:subProperty1>Sub Value 1</custom:subProperty1>
                    <custom:subProperty2>Sub Value 2</custom:subProperty2>
                </rdf:Description>
            </custom:additionalProperty>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

# Save the extended XMP file with even more complex structures
with open('./tmp/extended_xmp_file_extended.xmp', 'w') as file:
    file.write(xmp_content_extended)

print("Extended version of XMP file with even more complex structures has been generated and saved.")
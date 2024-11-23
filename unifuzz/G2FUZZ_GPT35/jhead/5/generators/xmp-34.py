import os

xmp_content = """<?xpacket begin='﻿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/">
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/" xmlns:exif="http://ns.adobe.com/exif/1.0/">
            <custom:extensibility>XMP files support the addition of custom metadata fields, allowing users to include specific information relevant to their files.</custom:extensibility>
            <custom:author>
                <rdf:Seq>
                    <rdf:li>John Doe</rdf:li>
                    <rdf:li>Jane Smith</rdf:li>
                </rdf:Seq>
            </custom:author>
            <custom:keywords>
                <rdf:Bag>
                    <rdf:li>keyword1</rdf:li>
                    <rdf:li>keyword2</rdf:li>
                    <rdf:li>keyword3</rdf:li>
                </rdf:Bag>
            </custom:keywords>
            <dc:title>Sample Title</dc:title>
            <exif:rating>5</exif:rating>
            <custom:additionalMetadata>
                <rdf:Description>
                    <custom:complexField>Complex Value</custom:complexField>
                    <custom:nestedField>
                        <rdf:Description>
                            <custom:subField1>Sub Value 1</custom:subField1>
                            <custom:subField2>Sub Value 2</custom:subField2>
                        </rdf:Description>
                    </custom:nestedField>
                </rdf:Description>
            </custom:additionalMetadata>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

with open('./tmp/example_extended.xmp', 'w') as file:
    file.write(xmp_content)

print("Extended XMP file with complex features created successfully.")
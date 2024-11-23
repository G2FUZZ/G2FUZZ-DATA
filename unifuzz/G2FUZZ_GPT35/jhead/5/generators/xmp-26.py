import os

xmp_content = """<?xpacket begin='﻿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/">
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
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

with open('./tmp/example_extended.xmp', 'w') as file:
    file.write(xmp_content)

print("Extended XMP file created successfully.")
import os

xmp_content = """<?xpacket begin='﻿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:custom="http://example.com/custom/" xmlns:exif="http://ns.adobe.com/exif/1.0/">
        <rdf:Description rdf:about="" >
            <dc:title>Advanced XMP File</dc:title>
            <custom:metadata>
                <rdf:Seq>
                    <rdf:li>
                        <custom:property1>Value 1</custom:property1>
                        <custom:property2>Value 2</custom:property2>
                    </rdf:li>
                    <rdf:li>
                        <custom:property1>Value 3</custom:property1>
                        <custom:property2>Value 4</custom:property2>
                    </rdf:li>
                </rdf:Seq>
            </custom:metadata>
            <exif:rating>10</exif:rating>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

with open('./tmp/advanced_xmp_file.xmp', 'w') as file:
    file.write(xmp_content)

print("Advanced XMP file with complex features created successfully.")
import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file with additional complex file features
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:custom="http://example.com/custom/">
            
            <dc:title>XMP File Example</dc:title>
            <dc:creator>
                <rdf:Seq>
                    <rdf:li>John Doe</rdf:li>
                    <rdf:li>Jane Smith</rdf:li>
                </rdf:Seq>
            </dc:creator>
            
            <custom:customField1>
                <rdf:Seq>
                    <rdf:li>Value 1</rdf:li>
                    <rdf:li>Value 2</rdf:li>
                </rdf:Seq>
            </custom:customField1>
            
            <custom:nestedField>
                <rdf:Description>
                    <custom:subField>Subfield Value</custom:subField>
                </rdf:Description>
            </custom:nestedField>
            
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

with open('./tmp/extended_feature_xmp.xmp', 'w') as file:
    file.write(xmp_content)

print("Extended XMP file generated successfully.")
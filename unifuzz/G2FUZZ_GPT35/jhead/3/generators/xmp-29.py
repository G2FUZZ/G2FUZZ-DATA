import os

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file content with complex features
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c132 79.159924, 2018/04/12-03:15:15        ">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmpNote="http://ns.adobe.com/xmp/note/"
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
            xmlns:pdf="http://ns.adobe.com/pdf/1.3/">
            <dc:title>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Hierarchical Structure</rdf:li>
                    <rdf:li xml:lang="en">Nested Metadata</rdf:li>
                </rdf:Alt>
            </dc:title>
            <xmp:CreatorTool>Adobe XMP Core 5.6-c132 79.159924, 2018/04/12-03:15:15</xmp:CreatorTool>
            <xmp:MetadataDate>2022-01-05T14:25:00Z</xmp:MetadataDate>
            <xmp:ModifyDate>2022-01-05T14:25:00Z</xmp:ModifyDate>
            <xmpMM:CustomProperty>
                <rdf:Bag>
                    <rdf:li>
                        <rdf:Description>
                            <rdf:value>This is a custom property value</rdf:value>
                            <rdf:type rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
                        </rdf:Description>
                    </rdf:li>
                </rdf:Bag>
            </xmpMM:CustomProperty>
            <pdf:Keywords>
                <rdf:Bag>
                    <rdf:li>keyword1</rdf:li>
                    <rdf:li>keyword2</rdf:li>
                    <rdf:li>keyword3</rdf:li>
                </rdf:Bag>
            </pdf:Keywords>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Save XMP file with complex features
file_path = './tmp/complex_xmp_file.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file with complex features saved at: {file_path}')
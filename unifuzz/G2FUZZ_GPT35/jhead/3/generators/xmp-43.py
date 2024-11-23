import os

# Create directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate complex XMP file content with nested elements and attributes
xmp_content = '''<?xpacket begin="�" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:LinkedData>https://example.com/linked_data</xmp:LinkedData>
            <xmp:CustomField1>Custom Value 1</xmp:CustomField1>
            <xmp:CustomField2>
                <xmp:SubField>Subfield Value</xmp:SubField>
                <xmp:SubFieldAttributes attr1="value1" attr2="value2">Nested Subfield with Attributes</xmp:SubFieldAttributes>
            </xmp:CustomField2>
            <xmp:CustomField3>
                <xmp:SubField>
                    <xmp:SubSubField>Deeply Nested Subfield</xmp:SubSubField>
                </xmp:SubField>
            </xmp:CustomField3>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Save XMP file with complex structure
file_path = './tmp/linked_data_more_complex.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file with more complex structure generated and saved at: {file_path}')
import os

# Define the content of the extended XMP file with nested elements and additional metadata
xmp_content_extended = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:custom="http://example.com/custom/">
            <xmp:CreatorTool>Python XMP Generator</xmp:CreatorTool>
            <xmp:CreateDate>2022-10-12T14:22:16+00:00</xmp:CreateDate>
            <custom:CustomField1>Custom Value 1</custom:CustomField1>
            <custom:CustomField2>Custom Value 2</custom:CustomField2>
            <custom:NestedElement>
                <custom:NestedField1>Nested Value 1</custom:NestedField1>
                <custom:NestedField2>Nested Value 2</custom:NestedField2>
            </custom:NestedElement>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Save the extended XMP file with the complex content
with open('./tmp/extended_complex_example.xmp', 'w') as file:
    file.write(xmp_content_extended)

print("Extended XMP file with complex structure generated and saved successfully.")
import os

# Define the content of the xmp file with more complex features
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c132 79.159725, 2016/09/14-01:09:01        ">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:dc="http://purl.org/dc/elements/1.1/"
             xmlns:custom="http://example.com/custom/">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:custom="http://example.com/custom/">
            <xmp:CreatorTool>My Custom XMP Generator</xmp:CreatorTool>
            <xmp:CreateDate>2022-10-15T08:30:00</xmp:CreateDate>
            <custom:CustomProperty1>Value1</custom:CustomProperty1>
            <custom:CustomNestedStructure>
                <custom:NestedProperty1>NestedValue1</custom:NestedProperty1>
                <custom:NestedProperty2>NestedValue2</custom:NestedProperty2>
            </custom:CustomNestedStructure>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Save the xmp content to a file
with open('./tmp/metadata_extended.xmp', 'w') as file:
    file.write(xmp_content)

print("Extended XMP file created successfully.")
import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP files with more complex file structures
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:CreatorTool>Advanced XMP Generator</xmp:CreatorTool>
            <xmp:CreateDate>2022-01-01T12:00:00</xmp:CreateDate>
            <xmp:Rating>5</xmp:Rating>
            <xmp:CustomMetadata>
                <xmp:CustomField1>Value1</xmp:CustomField1>
                <xmp:CustomField2>Value2</xmp:CustomField2>
            </xmp:CustomMetadata>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Save the generated XMP file
file_path = os.path.join(directory, 'sample_extended.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"Extended XMP file with more complex file structures generated and saved at: {file_path}")
import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP file with extended versioning information and nested elements
xmp_content = """
<?xpacket begin='﻿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about=''
            xmlns:xmp='http://ns.adobe.com/xap/1.0/'>
            <xmp:ModifyDate>2022-01-01T12:00:00</xmp:ModifyDate>
            <xmp:MetadataDate>2022-01-01T12:00:00</xmp:MetadataDate>
            <xmp:CreatorTool>Python XMP Generator</xmp:CreatorTool>
            <xmp:Version>1.0</xmp:Version>
            <xmp:CustomField1>Value1</xmp:CustomField1>
            <xmp:CustomField2>Value2</xmp:CustomField2>
            <xmp:NestedElement>
                <xmp:SubElement1>SubValue1</xmp:SubElement1>
                <xmp:SubElement2>SubValue2</xmp:SubElement2>
            </xmp:NestedElement>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

# Save the extended XMP file
file_path = os.path.join(directory, 'extended_metadata.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"Extended XMP file with complex file structures saved at: {file_path}")
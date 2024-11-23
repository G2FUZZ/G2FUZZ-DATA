import os

# Create a directory for storing xmp files
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp files with more complex file structures
xmp_data = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:Rating>5</xmp:Rating>
            <xmp:Embeddability>XMP metadata can be embedded within various file formats such as JPEG, PDF, and TIFF.</xmp:Embeddability>
            <xmp:CustomField1>Custom Value 1</xmp:CustomField1>
            <xmp:CustomField2>Custom Value 2</xmp:CustomField2>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Save the generated xmp file
with open('./tmp/extended_metadata.xmp', 'w') as file:
    file.write(xmp_data)

print("XMP file with extended metadata features has been generated and saved.")
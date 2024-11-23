import os

# Define the content to be written in the XMP file with multiple RDF descriptions and custom metadata fields
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:CustomField1>Value1</xmp:CustomField1>
            <xmp:CustomField2>Value2</xmp:CustomField2>
        </rdf:Description>
        <rdf:Description rdf:about="image.jpg" xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:title>Sample Image</dc:title>
            <dc:creator>John Doe</dc:creator>
            <dc:description>A sample description</dc:description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Write the XMP file with the defined content
with open('./tmp/example_extended.xmp', 'w') as file:
    file.write(xmp_content)

print("Extended XMP file generated successfully.")
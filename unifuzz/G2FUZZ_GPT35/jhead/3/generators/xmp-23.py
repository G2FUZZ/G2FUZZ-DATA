import os

# Define the content of the XMP file with more complex structure
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.4-c005 78.147326, 2012/08/23-13:03:03">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:custom="http://example.com/custom/">
            <custom:customField1>Custom Value 1</custom:customField1>
            <custom:customField2>Custom Value 2</custom:customField2>
            <custom:complexField>
                <custom:subField1>Subvalue 1</custom:subField1>
                <custom:subField2>Subvalue 2</custom:subField2>
            </custom:complexField>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the XMP file with more complex structure
with open('./tmp/custom_metadata_complex.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file with custom metadata and complex structure generated and saved successfully.")
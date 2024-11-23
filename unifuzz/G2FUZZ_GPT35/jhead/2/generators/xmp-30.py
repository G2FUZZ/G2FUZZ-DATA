import os

# Define the content of the extended XMP file with more complex structures
xmp_content_extended_complex = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140 79.160451, 2017/05/06-01:08:21">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:custom="http://example.com/custom/"
            custom:customField1="value1"
            custom:customField2="value2"
            custom:customField3="value3"
        >
            <custom:nestedField>
                <rdf:Bag>
                    <rdf:li>item1</rdf:li>
                    <rdf:li>item2</rdf:li>
                </rdf:Bag>
            </custom:nestedField>
            <custom:complexField>
                <rdf:Seq>
                    <rdf:li>
                        <rdf:Description>
                            <custom:subField>subValue1</custom:subField>
                        </rdf:Description>
                    </rdf:li>
                    <rdf:li>
                        <rdf:Description>
                            <custom:subField>subValue2</custom:subField>
                        </rdf:Description>
                    </rdf:li>
                </rdf:Seq>
            </custom:complexField>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Save the extended XMP file with the defined content
with open('./tmp/extended_custom_metadata_complex.xmp', 'w') as file:
    file.write(xmp_content_extended_complex)

print("Extended XMP file with custom metadata fields, nested structures, and complex fields generated and saved successfully.")
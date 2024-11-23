import os

# Define the content of the extended XMP file with even more complex structures
xmp_content_extended_super_complex = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140 79.160451, 2017/05/06-01:08:21        ">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:custom="http://example.com/custom/"
            custom:customField1="value1"
            custom:customField2="value2"
            custom:customField3="value3"
            custom:arrayField="item1, item2, item3"
            custom:multiLevelField="level1"
        >
            <custom:nestedField>
                <rdf:Seq>
                    <rdf:li>
                        <rdf:Description>
                            <custom:subField1>subValue1</custom:subField1>
                            <custom:subField2>subValue2</custom:subField2>
                            <custom:subArrayField>
                                <rdf:Bag>
                                    <rdf:li>subItem1</rdf:li>
                                    <rdf:li>subItem2</rdf:li>
                                </rdf:Bag>
                            </custom:subArrayField>
                        </rdf:Description>
                    </rdf:li>
                    <rdf:li>
                        <rdf:Description>
                            <custom:subField1>subValue3</custom:subField1>
                            <custom:subField2>subValue4</custom:subField2>
                            <custom:subArrayField>
                                <rdf:Bag>
                                    <rdf:li>subItem3</rdf:li>
                                    <rdf:li>subItem4</rdf:li>
                                </rdf:Bag>
                            </custom:subArrayField>
                        </rdf:Description>
                    </rdf:li>
                </rdf:Seq>
            </custom:nestedField>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Save the extended XMP file with the even more complex content
with open('./tmp/extended_custom_metadata_super_complex.xmp', 'w') as file:
    file.write(xmp_content_extended_super_complex)

print("Extended XMP file with custom metadata fields, nested structures, complex arrays, and multi-level fields generated and saved successfully.")
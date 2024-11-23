import os

# Define the extended XMP content with more complex file structures
extended_xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" xmlns:custom="http://example.com/custom/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:title>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Extended Complex XMP File</rdf:li>
                </rdf:Alt>
            </dc:title>
            <dc:description>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">This XMP file contains extended complex metadata information.</rdf:li>
                </rdf:Alt>
            </dc:description>
            <dc:creator>
                <rdf:Seq>
                    <rdf:li>John Doe</rdf:li>
                    <rdf:li>Jane Smith</rdf:li>
                </rdf:Seq>
            </dc:creator>
            <dc:subject>
                <rdf:Bag>
                    <rdf:li>Keyword1</rdf:li>
                    <rdf:li>Keyword2</rdf:li>
                    <rdf:li>Keyword3</rdf:li>
                </rdf:Bag>
            </dc:subject>
            <custom:customField1>Value1</custom:customField1>
            <custom:customField2>
                <custom:nestedField>
                    <custom:subField>Sub Value</custom:subField>
                </custom:nestedField>
            </custom:customField2>
            <custom:complexField>
                <rdf:Seq>
                    <rdf:li>
                        <rdf:Description>
                            <custom:subField1>Sub Value 1</custom:subField1>
                            <custom:subField2>Sub Value 2</custom:subField2>
                        </rdf:Description>
                    </rdf:li>
                    <rdf:li>
                        <rdf:Description>
                            <custom:subField1>Sub Value 3</custom:subField1>
                            <custom:subField2>Sub Value 4</custom:subField2>
                        </rdf:Description>
                    </rdf:li>
                </rdf:Seq>
            </custom:complexField>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the extended XMP file
with open('./tmp/extended_complex.xmp', 'w') as f:
    f.write(extended_xmp_content)

print("Extended Complex XMP file generated successfully in './tmp/' directory.")
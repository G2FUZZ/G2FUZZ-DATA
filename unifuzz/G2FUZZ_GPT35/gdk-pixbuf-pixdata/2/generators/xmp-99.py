import os

# Define the xmp content with multiple metadata fields and namespaces
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
            <xmpRights:UsageTerms>Rights Management: XMP allows for the inclusion of rights management information, such as usage rights and licensing terms, for digital assets.</xmpRights:UsageTerms>
            <xmpRights:Owner>
                <rdf:Seq>
                    <rdf:li>John Doe</rdf:li>
                    <rdf:li>Jane Doe</rdf:li>
                </rdf:Seq>
            </xmpRights:Owner>
        </rdf:Description>
        <rdf:Description rdf:about=""
            xmlns:custom="http://example.com/custom/">
            <custom:CustomField1>Custom Value 1</custom:CustomField1>
            <custom:CustomField2>Custom Value 2</custom:CustomField2>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Create a directory for saving xmp files if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the xmp content to a file
file_path = os.path.join(directory, 'extended_rights_management.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"Extended XMP file saved to {file_path}")
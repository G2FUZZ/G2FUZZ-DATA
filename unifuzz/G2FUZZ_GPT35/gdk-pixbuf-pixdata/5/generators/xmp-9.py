import os

# Define the content to be written in the XMP file
content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
            <xmpRights:Marked>True</xmpRights:Marked>
            <xmpRights:UsageTerms>
                XMP allows for the inclusion of rights management information for intellectual property protection.
            </xmpRights:UsageTerms>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Write the content to the XMP file
file_path = './tmp/rights_management.xmp'
with open(file_path, 'w') as file:
    file.write(content)

print(f'XMP file with rights management information has been generated and saved at: {file_path}')
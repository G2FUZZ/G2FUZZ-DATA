import os

# Define the XMP data
xmp_data = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
            <xmpRights:UsageTerms>XMP supports the inclusion of rights management information, such as usage rights and licensing terms, enabling better control and protection of intellectual property.</xmpRights:UsageTerms>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the XMP data to a file
file_path = './tmp/rights_management.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_data)

print(f"XMP file saved at: {file_path}")
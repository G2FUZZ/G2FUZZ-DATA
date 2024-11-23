import os

# Create a directory to store the xmp files
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp file with the specified features
xmp_content = """
<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about='' xmlns:xmpRights='http://ns.adobe.com/xap/1.0/rights/'>
            <xmpRights:UsageTerms>XMP can include rights-related information like usage terms and licensing details.</xmpRights:UsageTerms>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

# Save the generated xmp file
with open('./tmp/rights_management.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file with rights management feature generated and saved successfully.")
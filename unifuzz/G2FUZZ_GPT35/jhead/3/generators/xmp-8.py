import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the XMP file
xmp_content = """<?xpacket begin='﻿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about='' xmlns:dc='http://purl.org/dc/elements/1.1/'>
            <dc:rights>XMP supports the embedding of rights management information, including usage rights, licensing details, and restrictions related to the file.</dc:rights>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

# Save the XMP file
with open('./tmp/rights_management.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file with rights management information has been generated and saved.")
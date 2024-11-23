import os
from datetime import datetime

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Create XMP file content with complex structure
xmp_content = '''
<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Adobe XMP Core 5.6-c140 79.160451, 2019/07/25-13:54:36'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about=''>
            <dc:creator xmlns:dc='http://purl.org/dc/elements/1.1/'>John Doe</dc:creator>
            <dc:rights xmlns:dc='http://purl.org/dc/elements/1.1/'>Copyright 2022</dc:rights>
            <dc:subject xmlns:dc='http://purl.org/dc/elements/1.1/'>Python, XMP, Metadata</dc:subject>
            <dc:date xmlns:dc='http://purl.org/dc/elements/1.1/'>''' + str(datetime.now().isoformat()) + '''</dc:date>
            <custom:location xmlns:custom='http://example.com/custom/'>New York, USA</custom:location>
            <custom:rating xmlns:custom='http://example.com/custom/'>5 stars</custom:rating>
            <custom:tags xmlns:custom='http://example.com/custom/'>
                <custom:tag>Tag1</custom:tag>
                <custom:tag>Tag2</custom:tag>
                <custom:tag>Tag3</custom:tag>
            </custom:tags>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
'''

# Save content to XMP file
file_name = 'metadata_extended.xmp'
file_path = os.path.join(directory, file_name)

with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file '{file_name}' with extended metadata generated and saved in '{directory}'")
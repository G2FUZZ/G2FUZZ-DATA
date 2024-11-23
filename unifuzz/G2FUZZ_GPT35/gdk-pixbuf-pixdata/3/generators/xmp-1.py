import os
from datetime import datetime
from lxml import etree

# Create a directory if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate XMP metadata
metadata = {
    'Author': 'John Doe',
    'Copyright': '2022',
    'Keywords': ['Python', 'XMP', 'Metadata'],
    'CreationDate': datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
}

# Create XMP file for each feature
for feature, data in metadata.items():
    xmp_file_path = os.path.join(output_dir, f'{feature}.xmp')

    xpacket_start = b'<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>\n'
    xpacket_end = b'<?xpacket end="w"?>'
    xmp_data = f'<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140 79.160451, 2019/07/25-13:32:00">\n'
    xmp_data += f'    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n'
    xmp_data += f'        <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/">\n'
    
    for key, value in metadata.items():
        if isinstance(value, list):
            value = ', '.join(value)
        xmp_data += f'            <xmp:{key}>{value}</xmp:{key}>\n'
    
    xmp_data += f'        </rdf:Description>\n'
    xmp_data += f'    </rdf:RDF>\n'
    xmp_data += f'</x:xmpmeta>\n'

    with open(xmp_file_path, 'wb') as xmp_file:
        xmp_file.write(xpacket_start)
        xmp_file.write(xmp_data.encode())
        xmp_file.write(xpacket_end)

print('XMP files generated successfully.')
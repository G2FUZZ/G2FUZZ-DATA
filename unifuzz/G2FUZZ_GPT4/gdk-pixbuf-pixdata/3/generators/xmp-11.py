import os
from lxml import etree as ET

# Define the directory where the XMP files will be saved
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the XMP content focusing on the Searchability feature
xmp_data = {
    'dc:title': 'Enhanced Searchability Image',
    'dc:description': 'This image has been tagged with comprehensive metadata to improve searchability by providing detailed attributes that can be indexed and searched.',
    'dc:subject': ['searchability', 'metadata', 'indexing', 'file management']
}

# Create an XMP template
xmp_template = '''<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:dc="http://purl.org/dc/elements/1.1/">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <dc:title>{title}</dc:title>
            <dc:description>{description}</dc:description>
            <dc:subject>
                <rdf:Bag>
                    {subjects}
                </rdf:Bag>
            </dc:subject>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>'''

subjects_xml = ''.join([f'<rdf:li>{subject}</rdf:li>' for subject in xmp_data['dc:subject']])

xmp_content = xmp_template.format(title=xmp_data['dc:title'], 
                                  description=xmp_data['dc:description'],
                                  subjects=subjects_xml)

# Parse the XMP content to ensure its correctness
parser = ET.XMLParser(remove_blank_text=True)
xmp_tree = ET.fromstring(xmp_content, parser)

# Serialize the XMP content back into a string
xmp_str = ET.tostring(xmp_tree, pretty_print=True, encoding='utf-8', xml_declaration=True).decode()

# Define the output file path
output_file_path = os.path.join(output_dir, 'searchability_feature.xmp')

# Write the XMP content to a file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(xmp_str)

print(f'XMP file created at {output_file_path}')
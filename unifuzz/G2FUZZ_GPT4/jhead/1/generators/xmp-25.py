import os
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

# Ensure ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Manually declare namespaces in the root element
xmpmeta = Element('x:xmpmeta', {
    'xmlns:x': "adobe:ns:meta/",
    'xmlns:rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'xmlns:dc': "http://purl.org/dc/elements/1.1/",
    'xmlns:xmp': "http://ns.adobe.com/xap/1.0/"
})

rdf = SubElement(xmpmeta, 'rdf:RDF')
description = SubElement(rdf, 'rdf:Description', {
    'rdf:about': "",
    'dc:format': "image/jpeg",
    'xmp:CreatorTool': "Python Script"
})

# Set current date and time
current_datetime = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

# Add standard fields
SubElement(description, 'xmp:ModifyDate').text = current_datetime
SubElement(description, 'xmp:MetadataDate').text = current_datetime

# Add custom fields with complex structures
versionControl = SubElement(description, 'xmp:VersionControl')
seq = SubElement(versionControl, 'rdf:Seq')

# Example of adding multiple version control entries
versions = [
    {"version": "1.0", "modifier": "Author One", "modified": current_datetime, "changeDescription": "Initial creation"},
    {"version": "1.1", "modifier": "Author Two", "modified": current_datetime, "changeDescription": "Minor update"},
    {"version": "2.0", "modifier": "Author Three", "modified": current_datetime, "changeDescription": "Major revision"},
]

for v in versions:
    li = SubElement(seq, 'rdf:li')
    version_description = SubElement(li, 'rdf:Description')
    SubElement(version_description, 'xmp:version').text = v["version"]
    SubElement(version_description, 'xmp:modifier').text = v["modifier"]
    SubElement(version_description, 'xmp:modified').text = v["modified"]
    SubElement(version_description, 'xmp:changeDescription').text = v["changeDescription"]

# Create the XMP content
formatted_xmp_content = prettify(xmpmeta)

# Define the file path
file_path = os.path.join(output_dir, 'complex_version_control_metadata.xmp')

# Write the XMP content to a file
with open(file_path, 'w') as file:
    file.write(formatted_xmp_content)

print(f'XMP file created at {file_path}')
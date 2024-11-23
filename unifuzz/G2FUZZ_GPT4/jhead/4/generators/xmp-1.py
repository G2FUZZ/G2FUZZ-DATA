from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template
xmp_template = """
<x:xmpmeta xmlns:x="adobe:ns:meta/">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
        xmlns:xmp="http://ns.adobe.com/xap/1.0/">
        <xmp:CreatorTool>Python Script</xmp:CreatorTool>
        <xmp:CreateDate>2023-01-01T12:00:00</xmp:CreateDate>
        <xmp:ModifyDate>2023-01-01T12:00:00</xmp:ModifyDate>
        <xmp:MetadataDate>2023-01-01T12:00:00</xmp:MetadataDate>
        <xmp:standardization>
            Based on a framework developed by Adobe Systems, XMP standardizes the creation, processing, and interchange of standardized and custom metadata for digital documents and data sets. This ensures broad compatibility and understandability across different platforms and applications.
        </xmp:standardization>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
"""

# Parse the XMP template
xmp_data = etree.fromstring(xmp_template)

# Pretty print the XMP data
xmp_pretty = etree.tostring(xmp_data, pretty_print=True, encoding='UTF-8', xml_declaration=True)

# Define the file path
file_path = './tmp/feature_description.xmp'

# Write the XMP data to a file
with open(file_path, 'wb') as file:
    file.write(xmp_pretty)

print(f'XMP file created at {file_path}')
from lxml import etree as ET

# XMP basic structure
xmp_data = """
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:format>application/pdf</dc:format>
            <dc:description>Metadata Standardization: Enables a uniform format for metadata across various file formats, including PDF, JPEG, GIF, PNG, TIFF, and many others, facilitating easier management and sharing of information.</dc:description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
"""

# Parse the string to an XML element
root = ET.fromstring(xmp_data)

# Write to a file
output_path = './tmp/metadata_standardization.xmp'
with open(output_path, 'wb') as file:
    file.write(ET.tostring(root, pretty_print=True, encoding='UTF-8', xml_declaration=True))

print(f'XMP file saved at: {output_path}')
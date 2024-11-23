from lxml import etree
import os

# Ensure the target directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)  # Corrected argument name here

# XMP template with the specified feature
xmp_content = """
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/">
            <xmp:Synchronization>
                XMP can synchronize with other metadata formats embedded in files, such as Exif in images, ensuring that changes made to the XMP metadata are reflected in other metadata formats and vice versa.
            </xmp:Synchronization>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
""".strip()

# Create an XML tree and write the XMP file
root = etree.fromstring(xmp_content)
tree = etree.ElementTree(root)

# Define the output file path
output_file_path = os.path.join(output_dir, 'metadata_feature.xmp')

# Write the XMP file
with open(output_file_path, 'wb') as file:
    tree.write(file, pretty_print=True, xml_declaration=True, encoding='UTF-8')

print(f"XMP file generated at: {output_file_path}")
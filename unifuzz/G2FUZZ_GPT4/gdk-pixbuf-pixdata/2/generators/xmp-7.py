import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Ensure the target directory exists
target_dir = "./tmp/"
os.makedirs(target_dir, exist_ok=True)

# Define the XMP structure
def create_xmp_content():
    rdf_about = "uuid:faf5bdd5-ba3d-11da-ad31-d33d75182f1b"
    description_text = """
    7. **Standards Compliance**: XMP adheres to industry standards for metadata, making it compatible with a wide range of digital asset management (DAM) systems, libraries, and archives. This compliance ensures that metadata is not only preserved but also recognized and correctly processed by various systems.
    """
    
    # Root element
    xmpmeta = Element('x:xmpmeta', xmlns='adobe:ns:meta/')
    rdf = SubElement(xmpmeta, 'rdf:RDF', xmlns='http://www.w3.org/1999/02/22-rdf-syntax-ns#')

    # Description element
    description = SubElement(rdf, 'rdf:Description', {
        'rdf:about': rdf_about,
        'xmlns:dc': 'http://purl.org/dc/elements/1.1/'
    })

    # Adding the custom text as a description
    standards_compliance = SubElement(description, 'dc:description')
    standards_compliance.text = description_text
    
    return xmpmeta

# Generate and save the XMP file
def save_xmp_file(filename, xmp_content):
    file_path = os.path.join(target_dir, filename)
    ElementTree(xmp_content).write(file_path, encoding='utf-8', xml_declaration=True)
    print(f"File saved: {file_path}")

# Create XMP content
xmp_content = create_xmp_content()

# Save the file
save_xmp_file("example.xmp", xmp_content)
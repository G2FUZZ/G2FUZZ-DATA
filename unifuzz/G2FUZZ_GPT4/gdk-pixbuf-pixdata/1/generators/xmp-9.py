import os
from xml.dom.minidom import Document

def create_xmp_file(feature_text, file_name):
    # Create the XML document
    doc = Document()

    # Create the root element 'x:xmpmeta'
    xmpmeta = doc.createElement('x:xmpmeta')
    xmpmeta.setAttribute('xmlns:x', 'adobe:ns:meta/')
    doc.appendChild(xmpmeta)

    # Create 'rdf:RDF' element
    rdf = doc.createElement('rdf:RDF')
    rdf.setAttribute('xmlns:rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    xmpmeta.appendChild(rdf)

    # Create 'rdf:Description' element
    description = doc.createElement('rdf:Description')
    description.setAttribute('rdf:about', '')
    rdf.appendChild(description)

    # Create a custom tag for the feature
    feature = doc.createElement('Feature')
    feature_text_node = doc.createTextNode(feature_text)
    feature.appendChild(feature_text_node)
    description.appendChild(feature)

    # Generate the file content
    xmp_content = doc.toprettyxml(indent="  ")

    # Ensure the './tmp/' directory exists
    os.makedirs('./tmp/', exist_ok=True)

    # Create and write the content to an XMP file
    with open(f'./tmp/{file_name}.xmp', 'w', encoding='utf-8') as file:
        file.write(xmp_content)

# Feature text to be included in the XMP file
feature_text = "Open Standard: Adobe has made the XMP specification available to the public, encouraging its adoption across different industries and by various software developers. This openness has helped establish XMP as a widely accepted standard for metadata management."

# Generate the XMP file
create_xmp_file(feature_text, 'feature_open_standard')
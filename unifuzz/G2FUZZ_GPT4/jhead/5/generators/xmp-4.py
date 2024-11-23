import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import xml.dom.minidom

def create_xmp_file(feature_text, file_name):
    # Create the base structure of an XMP file
    rdf_RDF = Element('rdf:RDF')
    rdf_RDF.set('xmlns:rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    rdf_RDF.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
    
    rdf_Description = SubElement(rdf_RDF, 'rdf:Description')
    rdf_Description.set('rdf:about', '')
    
    dc_description = SubElement(rdf_Description, 'dc:description')
    dc_description.set('rdf:parseType', 'Literal')
    dc_description.text = feature_text
    
    # Convert the XML structure to a string
    rough_string = tostring(rdf_RDF, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_string = reparsed.toprettyxml(indent="  ")
    
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Write the pretty XML string to a file
    with open(f'./tmp/{file_name}.xmp', 'w') as xmp_file:
        xmp_file.write(pretty_string)

# Feature text to be included in the XMP file
feature_text = "XMP metadata can be embedded directly into the file it describes (for supported formats) or stored in an external sidecar file (typically with an .xmp extension) that accompanies the digital asset. This flexibility allows for metadata management without altering the original file for formats that do not natively support XMP embedding."

# Create an XMP file with the given feature text
create_xmp_file(feature_text, 'metadata_sidecar')
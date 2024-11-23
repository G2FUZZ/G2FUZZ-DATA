import os
import xml.etree.ElementTree as ET

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_xmp_file(filename):
    # Define namespaces
    namespaces = {
        'x': 'adobe:ns:meta/',
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'Iptc4xmpExt': 'http://iptc.org/std/Iptc4xmpExt/2008-02-29/',
        'exif': 'http://ns.adobe.com/exif/1.0/',
    }
    
    # Create an XML structure
    rdf = ET.Element('rdf:RDF', {'xmlns:rdf': namespaces['rdf']})
    
    # Description element with namespaces
    description_attrib = {f'{{{namespaces["rdf"]}}}about': 'UUID:...'}
    for ns, uri in namespaces.items():
        if ns not in ['rdf']:  # rdf is the default namespace, not needed in attributes
            description_attrib[f'{{{uri}}}xmlns:{ns}'] = uri
    description = ET.SubElement(rdf, 'rdf:Description', description_attrib)
    
    # Dublin Core schema example
    dc_title = ET.SubElement(description, f'{{{namespaces["dc"]}}}title')
    rdf_value = ET.SubElement(dc_title, 'rdf:Alt', {'xmlns:rdf': namespaces['rdf']})
    ET.SubElement(rdf_value, 'rdf:li', {'xml:lang': 'x-default'}).text = 'Document Title'
    
    # IPTC schema example
    iptc_creator = ET.SubElement(description, f'{{{namespaces["Iptc4xmpExt"]}}}Creator')
    rdf_seq = ET.SubElement(iptc_creator, 'rdf:Seq', {'xmlns:rdf': namespaces['rdf']})
    ET.SubElement(rdf_seq, 'rdf:li').text = 'Photographer Name'
    
    # Exif schema example
    exif_model = ET.SubElement(description, f'{{{namespaces["exif"]}}}model')
    exif_model.text = 'Camera Model'
    
    # Generate the tree and write to file
    tree = ET.ElementTree(rdf)
    tree.write(f'./tmp/{filename}', encoding='utf-8', xml_declaration=True)
    
# Example usage
create_xmp_file('example.xmp')
from lxml import etree
import os

def create_xmp_metadata(base_ns, additional_namespaces, properties):
    """
    Create an XMP metadata structure with dynamic properties and namespaces.
    """
    NSMAP = {'x': 'adobe:ns:meta/', 'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}
    NSMAP.update(additional_namespaces)
    rdf = etree.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=NSMAP)
    description = etree.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=NSMAP)
    
    for ns_prefix, prop_name, value, *attrs in properties:
        if attrs:
            attr_details = attrs[0]
        else:
            attr_details = {}
        
        if isinstance(value, list):
            # Handling for structured properties or arrays
            if 'structure' in attr_details:
                # Structured property
                parent_element = etree.SubElement(description, f"{{{NSMAP[ns_prefix]}}}{prop_name}")
                for item in value:
                    for k, v in item.items():
                        child = etree.SubElement(parent_element, f"{{{NSMAP[ns_prefix]}}}{k}")
                        child.text = v
            elif 'arrayType' in attr_details:
                # Array property (Bag or Seq)
                parent_element = etree.SubElement(description, f"{{{NSMAP[ns_prefix]}}}{prop_name}")
                array_type = etree.SubElement(parent_element, f"{{{NSMAP['rdf']}}}{attr_details['arrayType']}")
                for item in value:
                    li = etree.SubElement(array_type, f"{{{NSMAP['rdf']}}}li")
                    li.text = item
        else:
            # Simple property
            prop_element = etree.SubElement(description, f"{{{NSMAP[ns_prefix]}}}{prop_name}")
            prop_element.text = value
    
    return rdf

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define namespaces and properties
base_ns = "http://purl.org/dc/elements/1.1/"
additional_namespaces = {
    'dc': "http://purl.org/dc/elements/1.1/",
    'photoshop': "http://ns.adobe.com/photoshop/1.0/",
    'Iptc4xmpExt': "http://iptc.org/std/Iptc4xmpExt/2008-02-29/"
}

properties = [
    ('dc', 'title', 'Advanced Sample Image'),
    ('photoshop', 'ColorMode', 'RGB'),
    ('Iptc4xmpExt', 'LocationCreated', ['New York', 'Paris'], {'arrayType': 'Bag'}),
    ('dc', 'creator', [{'name': 'John Doe', 'role': 'Photographer'}], {'structure': True})
]

# Create XMP metadata
xmp_metadata = create_xmp_metadata(base_ns, additional_namespaces, properties)

# Wrap in xmpmeta element
xmpmeta = etree.Element('{adobe:ns:meta/}xmpmeta', nsmap={'x': 'adobe:ns:meta/'})
xmpmeta.append(xmp_metadata)

# Create an XML document and add the xpacket as a processing instruction
xml_doc = etree.ElementTree(xmpmeta)  # Create an ElementTree object from the xmpmeta element
xpacket_instruction = etree.ProcessingInstruction('xpacket', 'begin="" id="W5M0MpCehiHzreSzNTczkc9d"')
xml_doc.getroot().addprevious(xpacket_instruction)  # Add the processing instruction before the root element

# Write to file
file_path = './tmp/dynamic_advanced_xmp.xmp'
with open(file_path, 'wb') as file:
    file.write(etree.tostring(xml_doc, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f'Dynamic advanced XMP file saved to {file_path}')
from lxml import etree
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Base XMP structure with placeholders for dynamic content
xmp_template = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
           xmlns:dc="http://purl.org/dc/elements/1.1/"
           xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/"
           xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
           xmlns:customns="http://example.com/ns/custom/1.0/"
           xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
    <!-- Placeholder for image metadata -->
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

def create_custom_xmp(image_data):
    """
    Generate a custom XMP structure based on the provided image data.
    
    Args:
        image_data (list of dict): A list of dictionaries, each containing metadata for an image.
    """
    rdf_descriptions = []
    for image in image_data:
        description_elem = etree.Element('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description', nsmap={'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'})
        
        # Common attributes
        description_elem.set('{http://purl.org/dc/elements/1.1/}format', image.get('format', 'image/jpeg'))
        description_elem.set('{http://ns.adobe.com/photoshop/1.0/}ColorMode', str(image.get('ColorMode', '3')))
        description_elem.set('{http://ns.adobe.com/photoshop/1.0/}ICCProfile', image.get('ICCProfile', 'Adobe RGB (1998)'))
        
        # Custom attributes and complex structures like arrays
        for key, value in image.items():
            if key in ['format', 'ColorMode', 'ICCProfile']:
                continue  # Already processed
            
            if isinstance(value, dict):  # Nested structures
                sub_elem = etree.SubElement(description_elem, '{http://example.com/ns/custom/1.0/}' + key)
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, list):  # Array structures
                        sub_sub_elem = etree.SubElement(sub_elem, sub_key)
                        for item in sub_value:
                            # Correctly specify the namespace URI for 'rdf:li'
                            item_elem = etree.SubElement(sub_sub_elem, '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li')
                            item_elem.text = item['value']
                    else:
                        sub_sub_elem = etree.SubElement(sub_elem, sub_key)
                        sub_sub_elem.text = sub_value
            
            else:  # Simple key-value pairs
                description_elem.set('{http://example.com/ns/custom/1.0/}' + key, value)
        
        rdf_descriptions.append(description_elem)
    
    # Parse the base XMP structure
    xml_root = etree.fromstring(xmp_template)
    rdf_elem = xml_root.find('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF')
    
    # Append all descriptions to the RDF element
    for desc in rdf_descriptions:
        rdf_elem.append(desc)
    
    # Write to file
    file_path = './tmp/complex_extended_feature_description.xmp'
    with open(file_path, 'wb') as file:
        file.write(etree.tostring(xml_root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))
    
    print(f'Complex XMP file saved to {file_path}')

# Example data to generate XMP
image_data = [
    {
        'format': 'image/jpeg',
        'ColorMode': '3',
        'ICCProfile': 'Adobe RGB (1998)',
        'customField': 'Custom Value',
        'complexStructure': {
            'arrayExample': [
                {'type': 'rdf:li', 'value': 'Value 1'},
                {'type': 'rdf:li', 'value': 'Value 2'}
            ],
            'simpleField': 'Simple Value'
        }
    }
]

create_custom_xmp(image_data)
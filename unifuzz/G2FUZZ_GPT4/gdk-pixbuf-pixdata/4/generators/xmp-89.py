import os
import xml.etree.ElementTree as ET

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_advanced_xmp_file(filename):
    # Define namespaces
    namespaces = {
        'x': 'adobe:ns:meta/',
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'Iptc4xmpExt': 'http://iptc.org/std/Iptc4xmpExt/2008-02-29/',
        'exif': 'http://ns.adobe.com/exif/1.0/',
        'xmpRights': 'http://ns.adobe.com/xap/1.0/rights/',
        'photoshop': 'http://ns.adobe.com/photoshop/1.0/',
        'plus': 'http://ns.useplus.org/ldf/xmp/1.0/',
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
    ET.SubElement(rdf_value, 'rdf:li', {'xml:lang': 'x-default'}).text = 'Advanced Document Title'
    
    # IPTC schema example
    iptc_creator = ET.SubElement(description, f'{{{namespaces["Iptc4xmpExt"]}}}Creator')
    rdf_seq = ET.SubElement(iptc_creator, 'rdf:Seq', {'xmlns:rdf': namespaces['rdf']})
    ET.SubElement(rdf_seq, 'rdf:li').text = 'Advanced Photographer Name'  # Corrected line
    
    # Exif schema example, including GPS data
    exif_model = ET.SubElement(description, f'{{{namespaces["exif"]}}}model')
    exif_model.text = 'Advanced Camera Model'
    exif_gpsLatitude = ET.SubElement(description, f'{{{namespaces["exif"]}}}gpsLatitude')
    exif_gpsLatitude.text = '34;24.1N'
    exif_gpsLongitude = ET.SubElement(description, f'{{{namespaces["exif"]}}}gpsLongitude')
    exif_gpsLongitude.text = '118;40.1W'

    # Rights Management schema example
    rights_usageTerms = ET.SubElement(description, f'{{{namespaces["xmpRights"]}}}UsageTerms')
    rdf_alt = ET.SubElement(rights_usageTerms, 'rdf:Alt', {'xmlns:rdf': namespaces['rdf']})
    ET.SubElement(rdf_alt, 'rdf:li', {'xml:lang': 'x-default'}).text = 'Copyright information here'

    # Photoshop schema example
    photoshop_credit = ET.SubElement(description, f'{{{namespaces["photoshop"]}}}Credit')
    photoshop_credit.text = 'Photographer Agency'

    # PLUS (Picture Licensing Universal System) schema example
    plus_licenseInfoURL = ET.SubElement(description, f'{{{namespaces["plus"]}}}LicenseInfoURL')
    plus_licenseInfoURL.text = 'http://licenseinfourl.com'

    # Generate the tree and write to file with pretty print
    tree = ET.ElementTree(rdf)
    try:
        with open(f'./tmp/{filename}', 'wb') as file:
            file.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write(ET.tostring(rdf, encoding='utf-8', method='xml'))
    except IOError as e:
        print(f"Error writing file {filename}: {e}")

# Example usage
create_advanced_xmp_file('advanced_example.xmp')
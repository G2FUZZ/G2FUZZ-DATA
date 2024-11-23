import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_multilanguage_xmp(filename):
    # Create the root element
    xmpmeta = Element('x:xmpmeta', xmlns='adobe:ns:meta/')
    rdf = SubElement(xmpmeta, 'rdf:RDF', {'xmlns:rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'})

    # Description element with namespaces
    description = SubElement(rdf, 'rdf:Description', {
        'rdf:about': '',
        'xmlns:dc': 'http://purl.org/dc/elements/1.1/'
    })

    # Title element with multiple languages
    title = SubElement(description, 'dc:title')
    alt = SubElement(title, 'rdf:Alt')
    # English title
    li_en = SubElement(alt, 'rdf:li', {'xml:lang': 'en'})
    li_en.text = 'Example Title in English'
    # French title
    li_fr = SubElement(alt, 'rdf:li', {'xml:lang': 'fr'})
    li_fr.text = 'Exemple de Titre en Français'

    # Convert the ElementTree to bytes and decode to a string
    raw_xml = tostring(xmpmeta, 'utf-8')
    xml_str = '<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>\n' + raw_xml.decode('utf-8') + '\n<?xpacket end="w"?>'

    # Write to file
    with open(f'./tmp/{filename}', 'w', encoding='utf-8') as file:
        file.write(xml_str)

# Generate the XMP file
create_multilanguage_xmp('example.xmp')

print("XMP file with multi-language support generated and saved in ./tmp/")
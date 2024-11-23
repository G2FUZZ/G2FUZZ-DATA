import os
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring, register_namespace
from xml.dom.minidom import parseString

def create_advanced_xmp_file(file_name, languages_data, creator_info, keywords, rights_data, custom_data):
    """
    Creates an advanced XMP file with extensive internationalization support, creator information, keywords, rights statement, and custom metadata.
    
    Parameters:
    - file_name: The name of the file to be saved.
    - languages_data: A dictionary where keys are language codes and values are the text in that language for the title.
    - creator_info: A dictionary containing creator name and creation date.
    - keywords: A list of keywords associated with the file.
    - rights_data: A dictionary where keys are language codes and values are the text in that language for the rights statement.
    - custom_data: A dictionary containing custom metadata fields and their values.
    """
    
    # Define and register namespaces
    rdf_ns = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    dc_ns = "http://purl.org/dc/elements/1.1/"
    xmp_ns = "http://ns.adobe.com/xap/1.0/"
    custom_ns = "http://www.example.com/xmp/custom/"
    
    # Register namespaces to use them with ElementTree
    register_namespace('rdf', rdf_ns)
    register_namespace('dc', dc_ns)
    register_namespace('xmp', xmp_ns)
    register_namespace('custom', custom_ns)
    
    # Create root element
    rdf = Element(f'{{{rdf_ns}}}RDF')
    
    # Create description element with attributes for namespaces
    description = SubElement(rdf, f'{{{rdf_ns}}}Description', {
        f'{{{rdf_ns}}}about': '',
        f'{{{xmp_ns}}}CreatorTool': 'Custom XMP Writer',
        f'{{{xmp_ns}}}CreateDate': creator_info.get('date', datetime.now().isoformat()),
    })
    
    # Add creator
    creator = SubElement(description, f'{{{dc_ns}}}creator')
    seq = SubElement(creator, f'{{{rdf_ns}}}Seq')
    creator_name = SubElement(seq, f'{{{rdf_ns}}}li')
    creator_name.text = creator_info.get('name', 'Unknown')
    
    # Add title with different languages
    title = SubElement(description, f'{{{dc_ns}}}title')
    alt = SubElement(title, f'{{{rdf_ns}}}Alt')
    for lang, text in languages_data.items():
        li = SubElement(alt, f'{{{rdf_ns}}}li', {f'{{{rdf_ns}}}lang': lang})
        li.text = text
    
    # Add keywords
    subject = SubElement(description, f'{{{dc_ns}}}subject')
    bag = SubElement(subject, f'{{{rdf_ns}}}Bag')
    for keyword in keywords:
        li = SubElement(bag, f'{{{rdf_ns}}}li')
        li.text = keyword
    
    # Add rights statement in multiple languages
    rights = SubElement(description, f'{{{dc_ns}}}rights')
    alt_rights = SubElement(rights, f'{{{rdf_ns}}}Alt')
    for lang, text in rights_data.items():
        li = SubElement(alt_rights, f'{{{rdf_ns}}}li', {f'{{{rdf_ns}}}lang': lang})
        li.text = text
    
    # Add custom metadata
    for key, value in custom_data.items():
        custom_elem = SubElement(description, f'{{{custom_ns}}}{key}')
        custom_elem.text = value
    
    # Generate pretty XML string
    xml_bytes = tostring(rdf)
    xml_str = parseString(xml_bytes).toprettyxml(indent="  ")
    
    # Save to file
    file_path = os.path.join('./tmp/', file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(xml_str)

# Example usage
languages_data = {
    'en-US': 'Advanced Example Title in English',
    'fr-FR': 'Exemple avancé de titre en français',
    'es-ES': 'Ejemplo avanzado de título en español'
}

creator_info = {
    'name': 'John Doe',
    'date': '2023-01-01T12:00:00'
}

keywords = ['example', 'metadata', 'xmp']

rights_data = {
    'en-US': '©2023 John Doe. All rights reserved.',
    'fr-FR': '©2023 John Doe. Tous droits réservés.',
    'es-ES': '©2023 John Doe. Todos los derechos reservados.'
}

custom_data = {
    'Project': 'XMP Metadata Generation',
    'Version': '1.0'
}

create_advanced_xmp_file('advanced_example.xmp', languages_data, creator_info, keywords, rights_data, custom_data)
import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_xmp_metadata(custom_data, languages, conditions):
    """
    Generates XMP metadata with custom data, multilingual support, and conditional elements.
    
    :param custom_data: Dictionary of custom properties to include in the metadata.
    :param languages: Dictionary of language codes to descriptions for multilingual support.
    :param conditions: Dictionary of conditions for including conditional elements.
    :return: An XML string representing the XMP metadata.
    """
    ns_map = {
        'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        'dc': "http://purl.org/dc/elements/1.1/",
        'xmp': "http://ns.adobe.com/xap/1.0/",
        'photoshop': "http://ns.adobe.com/photoshop/1.0/",
        'xmpRights': "http://ns.adobe.com/xap/1.0/rights/",
        'xmpMM': "http://ns.adobe.com/xap/1.0/mm/",
        'dcTerms': "http://purl.org/dc/terms/",
        'customNS': "http://example.com/ns/custom/"
    }
    
    # Creating the root RDF element
    rdf = etree.Element("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF", nsmap=ns_map)
    
    # Creating the Description element
    description = etree.SubElement(rdf, "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description", nsmap=ns_map)
    description.set("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about", "")
    
    # Dynamic multilingual descriptions
    for lang, desc in languages.items():
        desc_element = etree.SubElement(description, "{http://purl.org/dc/elements/1.1/}description", nsmap=ns_map)
        desc_element.set("{http://www.w3.org/XML/1998/namespace}lang", lang)
        desc_element.text = desc
    
    # Conditional elements based on provided conditions
    if conditions.get('include_custom_element', False):
        custom_element = etree.SubElement(description, "{http://example.com/ns/custom/}CustomProperty", nsmap=ns_map)
        custom_element.text = "Custom Value"
    
    # Convert to string
    return etree.tostring(rdf, pretty_print=True, encoding='UTF-8', xml_declaration=True).decode('UTF-8')

def save_xmp_file(file_path, content):
    """
    Saves the XMP content to a file.

    :param file_path: The path where the file will be saved.
    :param content: The content to save in the file.
    """
    with open(file_path, 'w', encoding='UTF-8') as file:
        file.write(content)

# Example usage
custom_data = {'CustomTag': 'CustomValue'}
languages = {'en-US': 'Example file with custom and conditional elements', 'fr-FR': 'Exemple de fichier avec éléments personnalisés et conditionnels'}
conditions = {'include_custom_element': True}

xmp_content = create_xmp_metadata(custom_data, languages, conditions)
xmp_file_path = './tmp/advanced_metadata.xmp'
save_xmp_file(xmp_file_path, xmp_content)
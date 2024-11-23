import os
from xml.etree.ElementTree import Element, SubElement, tostring, register_namespace
from xml.dom.minidom import parseString

def create_xmp_file(file_name, languages_data):
    """
    Creates an XMP file with internationalization support for the given languages.
    
    Parameters:
    - file_name: The name of the file to be saved.
    - languages_data: A dictionary where keys are language codes and values are the text in that language.
    """
    
    # Define and register namespaces
    rdf_ns = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    dc_ns = "http://purl.org/dc/elements/1.1/"
    
    # It's important to register namespaces to use them with ElementTree
    register_namespace('rdf', rdf_ns)
    register_namespace('dc', dc_ns)
    
    # Create root element without manually setting namespace declarations as attributes
    rdf = Element(f'{{{rdf_ns}}}RDF')
    
    # Create description element
    description = SubElement(rdf, f'{{{rdf_ns}}}Description')
    
    # Add title with different languages
    title = SubElement(description, f'{{{dc_ns}}}title')
    alt = SubElement(title, f'{{{rdf_ns}}}Alt')
    
    for lang, text in languages_data.items():
        li = SubElement(alt, f'{{{rdf_ns}}}li', {f'{{{rdf_ns}}}lang': lang})
        li.text = text
    
    # Generate pretty XML string
    xml_bytes = tostring(rdf)
    xml_str = parseString(xml_bytes).toprettyxml(indent="  ")
    
    # Save to file
    file_path = os.path.join('./tmp/', file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(xml_str)

# Example usage
languages_data = {
    'en-US': 'Example Title in English',
    'fr-FR': 'Exemple de titre en français',
    'es-ES': 'Ejemplo de título en español'
}

create_xmp_file('example.xmp', languages_data)
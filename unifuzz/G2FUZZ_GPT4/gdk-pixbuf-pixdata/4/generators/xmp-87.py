import os
from xml.dom.minidom import Document

def create_xmp_file(directory, filename, metadata):
    """
    Generates an XMP file with complex structures including custom namespaces,
    multiple descriptions, and nested elements.

    :param directory: The directory where the XMP file will be saved.
    :param filename: The name of the XMP file.
    :param metadata: A dictionary containing metadata to be included in the XMP file.
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define the XMP file path
    file_path = os.path.join(directory, filename)

    # Create a minidom document
    doc = Document()

    # Create RDF root element
    rdf = doc.createElementNS('http://www.w3.org/1999/02/22-rdf-syntax-ns#', 'rdf:RDF')
    doc.appendChild(rdf)

    # Namespace attributes for the RDF element
    namespaces = {
        "xmlns:rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "xmlns:xmp": "http://ns.adobe.com/xap/1.0/",
        "xmlns:dc": "http://purl.org/dc/elements/1.1/",
        "xmlns:exif": "http://ns.adobe.com/exif/1.0/",
        "xmlns:custom": "http://example.com/ns/"
    }
    for key, value in namespaces.items():
        rdf.setAttribute(key, value)

    for description in metadata:
        # Create Description element
        desc = doc.createElement('rdf:Description')
        rdf.appendChild(desc)

        # Set about attribute (optional)
        if 'about' in description:
            desc.setAttribute('rdf:about', description['about'])

        # Add properties to the Description
        for prop, value in description['properties'].items():
            if isinstance(value, list):  # Check if value is a list to create a Bag
                propElement = doc.createElement(prop)
                desc.appendChild(propElement)

                # Create a Bag for the list
                bag = doc.createElement('rdf:Bag')
                propElement.appendChild(bag)

                for item in value:
                    li = doc.createElement('rdf:li')
                    li.appendChild(doc.createTextNode(item))
                    bag.appendChild(li)
            else:
                propElement = doc.createElement(prop)
                propElement.appendChild(doc.createTextNode(value))
                desc.appendChild(propElement)

    # Write to file
    with open(file_path, 'w') as file:
        file.write(doc.toprettyxml(indent="  "))

    print(f'XMP file saved to {file_path}')

# Example usage
directory = './tmp/'
filename = 'complex_features.xmp'
metadata = [
    {
        'about': '',
        'properties': {
            'dc:title': 'Complex XMP Example',
            'dc:creator': ['John Doe', 'Jane Doe'],
            'dc:description': 'This is an example of a complex XMP file with custom namespaces and structures.',
            'custom:exampleProperty': 'Example Value',
            'custom:exampleList': ['Value 1', 'Value 2']
        }
    },
    # Additional rdf:Description blocks can be added here
]

create_xmp_file(directory, filename, metadata)
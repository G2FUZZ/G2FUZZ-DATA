import os
from xml.dom.minidom import getDOMImplementation

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a minimal XMP structure with the correct RDF namespace
impl = getDOMImplementation()
document = impl.createDocument("http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf:RDF", None)

# Set the necessary namespaces as attributes
document.documentElement.setAttribute("xmlns:x", "adobe:ns:meta/")
document.documentElement.setAttribute("x:xmptk", "Adobe XMP Core 5.6-c014 79.160451, 2017/05/06-01:08:21")
document.documentElement.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")

# Dublin Core Metadata with multiple languages
dc_description = document.createElement("rdf:Description")
dc_description.setAttribute("rdf:about", "")
dc_description.setAttribute("xmlns:dc", "http://purl.org/dc/elements/1.1/")

# Adding a Dublin Core title element with multiple languages
dc_title = document.createElement("dc:title")
rdf_value = document.createElement("rdf:Alt")

# English title
rdf_li_en = document.createElement("rdf:li")
rdf_li_en.setAttribute("xml:lang", "en")
rdf_li_en.appendChild(document.createTextNode("Sample XMP File - English"))
rdf_value.appendChild(rdf_li_en)

# French title
rdf_li_fr = document.createElement("rdf:li")
rdf_li_fr.setAttribute("xml:lang", "fr")
rdf_li_fr.appendChild(document.createTextNode("Fichier XMP d'exemple - Français"))
rdf_value.appendChild(rdf_li_fr)

dc_title.appendChild(rdf_value)
dc_description.appendChild(dc_title)

# Rights Management Metadata with xsi:type
rights_description = document.createElement("rdf:Description")
rights_description.setAttribute("rdf:about", "")
rights_description.setAttribute("xmlns:xmpRights", "http://ns.adobe.com/xap/1.0/rights/")

# Adding a Rights Management element (WebStatement) with xsi:type
rights_web_statement = document.createElement("xmpRights:WebStatement")
rights_web_statement.setAttribute("xsi:type", "rdf:Resource")
rights_web_statement.appendChild(document.createTextNode("http://example.com/rights"))
rights_description.appendChild(rights_web_statement)

# Custom metadata with nested structures
custom_description = document.createElement("rdf:Description")
custom_description.setAttribute("rdf:about", "")
custom_description.setAttribute("xmlns:customNS", "http://example.com/ns/")

# Adding a complex custom metadata element with nested structure
custom_element = document.createElement("customNS:ComplexProperty")
custom_nested_element = document.createElement("rdf:Bag")

# Nested items
for i in range(1, 4):
    nested_item = document.createElement("rdf:li")
    nested_item.appendChild(document.createTextNode(f"Nested Value {i}"))
    custom_nested_element.appendChild(nested_item)

custom_element.appendChild(custom_nested_element)
custom_description.appendChild(custom_element)

# Appending the created elements to the document
document.documentElement.appendChild(dc_description)
document.documentElement.appendChild(rights_description)
document.documentElement.appendChild(custom_description)

# Generate the XMP file content
xmp_content = document.toprettyxml(indent="  ")

# Save the XMP file
file_path = './tmp/complex_structure_with_types_and_languages.xmp'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(xmp_content)

print(f"XMP file saved at: {file_path}")
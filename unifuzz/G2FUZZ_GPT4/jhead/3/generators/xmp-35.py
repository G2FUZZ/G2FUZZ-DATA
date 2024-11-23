import os
from xml.dom.minidom import getDOMImplementation

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a minimal XMP structure with the correct RDF namespace
impl = getDOMImplementation()
# The namespace URI for RDF is "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
# Correcting the document creation to not use a prefix in the qualified name
document = impl.createDocument("http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf:RDF", None)

# Set the necessary namespaces as attributes
document.documentElement.setAttribute("xmlns:x", "adobe:ns:meta/")
document.documentElement.setAttribute("x:xmptk", "Adobe XMP Core 5.6-c014 79.160451, 2017/05/06-01:08:21")

# The rest of the code remains largely the same, appending elements to the rdf:RDF element correctly

# Dublin Core Metadata
dc_description = document.createElement("rdf:Description")
dc_description.setAttribute("rdf:about", "")
dc_description.setAttribute("xmlns:dc", "http://purl.org/dc/elements/1.1/")

# Adding a simple Dublin Core element (title)
dc_title = document.createElement("dc:title")
rdf_value = document.createElement("rdf:Alt")
rdf_li = document.createElement("rdf:li")
rdf_li.setAttribute("xml:lang", "x-default")
rdf_li.appendChild(document.createTextNode("Sample XMP File"))
rdf_value.appendChild(rdf_li)
dc_title.appendChild(rdf_value)

dc_description.appendChild(dc_title)

# Rights Management Metadata
rights_description = document.createElement("rdf:Description")
rights_description.setAttribute("rdf:about", "")
rights_description.setAttribute("xmlns:xmpRights", "http://ns.adobe.com/xap/1.0/rights/")

# Adding a Rights Management element (WebStatement)
rights_web_statement = document.createElement("xmpRights:WebStatement")
rights_web_statement.appendChild(document.createTextNode("http://example.com/rights"))
rights_description.appendChild(rights_web_statement)

# Custom metadata
custom_description = document.createElement("rdf:Description")
custom_description.setAttribute("rdf:about", "")
custom_description.setAttribute("xmlns:customNS", "http://example.com/ns/")

# Adding a custom metadata element
custom_element = document.createElement("customNS:CustomProperty")
custom_element.appendChild(document.createTextNode("Custom Value"))
custom_description.appendChild(custom_element)

# Appending the created elements to the document
document.documentElement.appendChild(dc_description)
document.documentElement.appendChild(rights_description)
document.documentElement.appendChild(custom_description)

# Generate the XMP file content
xmp_content = document.toprettyxml(indent="  ")

# Save the XMP file
file_path = './tmp/complex_structure.xmp'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(xmp_content)

print(f"XMP file saved at: {file_path}")
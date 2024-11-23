import os
from xml.dom.minidom import getDOMImplementation

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a minimal XMP structure
impl = getDOMImplementation()
# Adjusted to not use namespace URI and doctype in the creation of the document
document = impl.createDocument(None, "xmpmeta", None)  # Simplified root element name

# Set the necessary namespace as an attribute
document.documentElement.setAttribute("xmlns:x", "adobe:ns:meta/")
document.documentElement.setAttribute("x:xmptk", "Adobe XMP Core 5.6-c014 79.160451, 2017/05/06-01:08:21")

rdf = document.createElement("rdf:RDF")
rdf.setAttribute("xmlns:rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")

# Add a description about the standardization
desc = document.createElement("rdf:Description")
desc.setAttribute("rdf:about", "")
comment = document.createComment(
    " Standardization: XMP is based on XML (eXtensible Markup Language), "
    "making it a standardized format for embedding, processing, and exchanging metadata."
)
desc.appendChild(comment)
rdf.appendChild(desc)
document.documentElement.appendChild(rdf)

# Generate the XMP file content
xmp_content = document.toprettyxml(indent="  ")

# Save the XMP file
file_path = './tmp/standardization_feature.xmp'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(xmp_content)

print(f"XMP file saved at: {file_path}")
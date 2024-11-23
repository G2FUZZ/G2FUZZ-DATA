import os
from xml.dom.minidom import Document

# Create the XMP document
doc = Document()

# Create rdf:RDF element as the root
rdf = doc.createElementNS("http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf:RDF")
doc.appendChild(rdf)

# Create rdf:Description element
description = doc.createElement("rdf:Description")
description.setAttributeNS("http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf:about", "")
rdf.appendChild(description)

# Add a custom property (feature)
feature = doc.createElement("xmp:Standardization")
text = doc.createTextNode("XMP is based on XML, making it both readable and writable by humans and machines. This adherence to a standard ensures broad compatibility and ease of processing.")
feature.appendChild(text)
description.appendChild(feature)

# Save the document to a file
xmp_path = './tmp/feature.xmp'
os.makedirs(os.path.dirname(xmp_path), exist_ok=True)

with open(xmp_path, "w") as file:
    file.write(doc.toprettyxml(indent="  "))

print(f"XMP file saved to {xmp_path}")
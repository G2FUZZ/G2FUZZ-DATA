import os
from xml.dom.minidom import Document

# Create the XMP document
doc = Document()

# Define namespaces
ns_rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
ns_xmp = "http://ns.adobe.com/xap/1.0/"
ns_dc = "http://purl.org/dc/elements/1.1/"
ns_custom = "http://example.com/xmp/custom/"

# Create rdf:RDF element as the root
rdf = doc.createElementNS(ns_rdf, "rdf:RDF")
doc.appendChild(rdf)

# Create rdf:Description element for XMP Basic properties
description_xmp = doc.createElementNS(ns_xmp, "rdf:Description")
description_xmp.setAttributeNS(ns_rdf, "rdf:about", "")
description_xmp.setAttributeNS("http://www.w3.org/2000/xmlns/", "xmlns:xmp", ns_xmp)
rdf.appendChild(description_xmp)

# Add CreatorTool to the XMP description
creator_tool = doc.createElement("xmp:CreatorTool")
creator_tool_text = doc.createTextNode("Advanced Code Editor 1.0")
creator_tool.appendChild(creator_tool_text)
description_xmp.appendChild(creator_tool)

# Create rdf:Description element for Dublin Core properties
description_dc = doc.createElementNS(ns_dc, "rdf:Description")
description_dc.setAttributeNS(ns_rdf, "rdf:about", "")
description_dc.setAttributeNS("http://www.w3.org/2000/xmlns/", "xmlns:dc", ns_dc)
rdf.appendChild(description_dc)

# Add a Title to the DC description
title = doc.createElement("dc:title")
title_bag = doc.createElementNS(ns_rdf, "rdf:Bag")
title_li = doc.createElementNS(ns_rdf, "rdf:li")
title_li_text = doc.createTextNode("Advanced XMP Example")
title_li.appendChild(title_li_text)
title_bag.appendChild(title_li)
title.appendChild(title_bag)
description_dc.appendChild(title)

# Create rdf:Description element for custom properties
description_custom = doc.createElementNS(ns_custom, "rdf:Description")
description_custom.setAttributeNS(ns_rdf, "rdf:about", "")
description_custom.setAttributeNS("http://www.w3.org/2000/xmlns/", "xmlns:custom", ns_custom)
rdf.appendChild(description_custom)

# Add a custom property with nested structure
complex_feature = doc.createElement("custom:ComplexFeature")
complex_feature_seq = doc.createElementNS(ns_rdf, "rdf:Seq")

# Add multiple items to the complex feature
for i in range(1, 4):
    item = doc.createElementNS(ns_rdf, "rdf:li")
    item_text = doc.createTextNode(f"Feature Detail {i}")
    item.appendChild(item_text)
    complex_feature_seq.appendChild(item)

complex_feature.appendChild(complex_feature_seq)
description_custom.appendChild(complex_feature)

# Save the document to a file
xmp_path = './tmp/advanced_feature.xmp'
os.makedirs(os.path.dirname(xmp_path), exist_ok=True)

with open(xmp_path, "w") as file:
    file.write(doc.toprettyxml(indent="  "))

print(f"XMP file saved to {xmp_path}")
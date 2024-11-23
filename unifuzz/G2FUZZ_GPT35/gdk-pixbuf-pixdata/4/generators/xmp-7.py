import os
from xml.etree import ElementTree as ET

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the XMP metadata content
xmp_content = """
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
    <xmpRights:UsageTerms>Usage terms here</xmpRights:UsageTerms>
    <xmpRights:Licenses>
      <rdf:Bag>
        <rdf:li>Licenses here</rdf:li>
      </rdf:Bag>
    </xmpRights:Licenses>
    <xmpRights:DigitalRightsManagement>DRM details here</xmpRights:DigitalRightsManagement>
  </rdf:Description>
</rdf:RDF>
"""

# Save the XMP file
file_path = os.path.join(directory, 'rights_management.xmp')
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file saved at: {file_path}")
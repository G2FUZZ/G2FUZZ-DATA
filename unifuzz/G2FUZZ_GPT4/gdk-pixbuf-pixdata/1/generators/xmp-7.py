from lxml import etree
import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument here

# Define the XMP template with placeholders for the metadata
xmp_template = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP toolkit">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:xmp="http://ns.adobe.com/xap/1.0/"
    xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
    dc:creator="{creator}"
    dc:description="{description}"
    xmp:CreateDate="{create_date}"
    xmp:ModifyDate="{modify_date}"
    xmpRights:UsageTerms="{usage_terms}"
    xmpRights:Copyrighted="{copyrighted}"
    xmpRights:Owner="{owner}">
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Metadata to be included in the XMP file
metadata = {
    "creator": "John Doe",
    "description": "A comprehensive description of the file content.",
    "create_date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "modify_date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "usage_terms": "This file is licensed under XYZ terms.",
    "copyrighted": "True",
    "owner": "John Doe"
}

# Format the XMP template with the provided metadata
xmp_data = xmp_template.format(**metadata)

# Save the XMP data to a file
file_path = './tmp/descriptive_metadata.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_data)

print(f"XMP file saved at {file_path}")
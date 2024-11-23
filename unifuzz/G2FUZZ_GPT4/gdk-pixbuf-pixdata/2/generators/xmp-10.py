import os
from datetime import datetime
from lxml import etree

# Create the ./tmp/ directory if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# XMP basic structure
xmp_template = """
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:xmp="http://ns.adobe.com/xap/1.0/">
   <dc:format>application/pdf</dc:format>
   <xmp:ModifyDate>{modify_date}</xmp:ModifyDate>
   <xmp:CreatorTool>Python Script</xmp:CreatorTool>
   <xmp:MetadataDate>{metadata_date}</xmp:MetadataDate>
   <xmp:VersionControl>
    <rdf:Seq>
     <rdf:li>Initial version</rdf:li>
     <rdf:li>Revised version - added section 2</rdf:li>
     <rdf:li>Final version - proofread and corrected</rdf:li>
    </rdf:Seq>
   </xmp:VersionControl>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
"""

# Replace placeholders with current date and time
current_datetime = datetime.now().isoformat()
xmp_content = xmp_template.format(modify_date=current_datetime, metadata_date=current_datetime)

# Convert the string to an XML element
xmp_element = etree.fromstring(xmp_content)

# Write the XMP file
xmp_file_path = os.path.join(output_dir, 'document_version_history.xmp')
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(etree.tostring(xmp_element, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f"XMP file created at: {xmp_file_path}")
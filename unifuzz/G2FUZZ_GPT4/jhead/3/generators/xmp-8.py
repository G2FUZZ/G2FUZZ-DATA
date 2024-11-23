import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template with history tracking
xmp_template = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
       xmlns:xmp="http://ns.adobe.com/xap/1.0/"
       xmlns:dc="http://purl.org/dc/elements/1.1/"
       xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/">
   <dc:format>image/jpeg</dc:format>
   <xmp:ModifyDate>{modify_date}</xmp:ModifyDate>
   <xmp:CreatorTool>Example Creator</xmp:CreatorTool>
   <xmpMM:History>
    <rdf:Seq>
     <rdf:li rdf:parseType="Resource">
      <stEvt:action>created</stEvt:action>
      <stEvt:instanceID>xmp.iid:123456</stEvt:instanceID>
      <stEvt:when>{creation_date}</stEvt:when>
      <stEvt:softwareAgent>Example Creator</stEvt:softwareAgent>
     </rdf:li>
     <rdf:li rdf:parseType="Resource">
      <stEvt:action>modified</stEvt:action>
      <stEvt:instanceID>xmp.iid:7891011</stEvt:instanceID>
      <stEvt:when>{modify_date}</stEvt:when>
      <stEvt:softwareAgent>Example Modifier</stEvt:softwareAgent>
     </rdf:li>
    </rdf:Seq>
   </xmpMM:History>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Current date-time in ISO format for history tracking
current_date_iso = datetime.now().isoformat()

# Fill in the template
xmp_content = xmp_template.format(modify_date=current_date_iso, creation_date=current_date_iso)

# Define the file name
file_name = './tmp/example.xmp'

# Write the XMP content to a file
with open(file_name, 'w') as file:
    file.write(xmp_content)

print(f'XMP file saved as {file_name}')
import os
from datetime import datetime

# Define the directory to save the XMP file
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the XMP content with history tracking
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/">
         <dc:format>image/jpeg</dc:format>
         <xmp:CreatorTool>Example Creator Tool</xmp:CreatorTool>
         <xmp:CreateDate>2023-01-01T12:00:00</xmp:CreateDate>
         <xmpMM:History>
            <rdf:Seq>
               <rdf:li rdf:parseType="Resource">
                  <stEvt:action>created</stEvt:action>
                  <stEvt:instanceID>xmp.iid:1234</stEvt:instanceID>
                  <stEvt:when>2023-01-01T12:00:00</stEvt:when>
                  <stEvt:softwareAgent>Example Creator Tool</stEvt:softwareAgent>
                  <stEvt:changed>/</stEvt:changed>
               </rdf:li>
               <rdf:li rdf:parseType="Resource">
                  <stEvt:action>edited</stEvt:action>
                  <stEvt:instanceID>xmp.iid:5678</stEvt:instanceID>
                  <stEvt:when>2023-01-02T12:00:00</stEvt:when>
                  <stEvt:softwareAgent>Example Editor Tool</stEvt:softwareAgent>
                  <stEvt:changed>/metadata</stEvt:changed>
               </rdf:li>
            </rdf:Seq>
         </xmpMM:History>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Define the file name
file_name = 'example.xmp'

# Write the XMP content to a file in the specified directory
full_path = os.path.join(output_dir, file_name)
with open(full_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file saved to {full_path}')
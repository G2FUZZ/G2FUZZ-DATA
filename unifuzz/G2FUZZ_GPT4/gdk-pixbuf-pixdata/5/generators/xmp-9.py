import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate the XMP content
xmp_content = f"""<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c014 79.159824, 2016/09/14-01:09:01        ">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/">
         <xmp:CreateDate>{datetime.now().isoformat()}</xmp:CreateDate>
         <xmp:ModifyDate>{datetime.now().isoformat()}</xmp:ModifyDate>
         <xmpMM:History>
            <rdf:Seq>
               <rdf:li rdf:parseType="Resource">
                  <stEvt:action>created</stEvt:action>
                  <stEvt:instanceID>xmp.iid:123456</stEvt:instanceID>
                  <stEvt:when>{datetime.now().isoformat()}</stEvt:when>
                  <stEvt:softwareAgent>Python Script</stEvt:softwareAgent>
               </rdf:li>
            </rdf:Seq>
         </xmpMM:History>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Save the XMP content to a file
file_path = './tmp/example.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file created at: {file_path}')
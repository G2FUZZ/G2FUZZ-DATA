import os
from datetime import datetime

# Function to add a history event
def add_history_event(action, instance_id, software_agent):
    return f"""
               <rdf:li rdf:parseType="Resource">
                  <stEvt:action>{action}</stEvt:action>
                  <stEvt:instanceID>{instance_id}</stEvt:instanceID>
                  <stEvt:when>{datetime.now().isoformat()}</stEvt:when>
                  <stEvt:softwareAgent>{software_agent}</stEvt:softwareAgent>
               </rdf:li>
           """

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Determine the file type and set custom metadata accordingly
file_type = 'photo'  # Example file type
custom_metadata = ''
if file_type == 'photo':
    custom_metadata = """
            <dc:format>image/jpeg</dc:format>
            <photoshop:ColorMode>3</photoshop:ColorMode>  # 3 corresponds to RGB
            """
elif file_type == 'document':
    custom_metadata = """
            <dc:format>application/pdf</dc:format>
            <xmp:CreatorTool>Adobe Acrobat</xmp:CreatorTool>
            """

# Generate the XMP content with conditional metadata and multiple history entries
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
         {custom_metadata}
         <xmpMM:History>
            <rdf:Seq>
               {add_history_event('created', 'xmp.iid:123456', 'Python Script')}
               {add_history_event('modified', 'xmp.iid:789012', 'Python Script')}
            </rdf:Seq>
         </xmpMM:History>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Save the XMP content to a file
file_path = './tmp/complex_example.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'Complex XMP file created at: {file_path}')
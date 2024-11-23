import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the metadata content, including timestamps and history
xmp_content = f"""<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
            xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#">
            <dc:format>application/pdf</dc:format>
            <xmp:CreateDate>{datetime.now().isoformat()}</xmp:CreateDate>
            <xmp:ModifyDate>{datetime.now().isoformat()}</xmp:ModifyDate>
            <xmp:MetadataDate>{datetime.now().isoformat()}</xmp:MetadataDate>
            <xmpMM:History>
                <rdf:Seq>
                    <rdf:li rdf:parseType="Resource">
                        <stEvt:action>created</stEvt:action>
                        <stEvt:instanceID>xmp.iid:123456</stEvt:instanceID>
                        <stEvt:when>{datetime.now().isoformat()}</stEvt:when>
                        <stEvt:softwareAgent>Python Script</stEvt:softwareAgent>
                    </rdf:li>
                    <rdf:li rdf:parseType="Resource">
                        <stEvt:action>modified</stEvt:action>
                        <stEvt:instanceID>xmp.iid:789012</stEvt:instanceID>
                        <stEvt:when>{datetime.now().isoformat()}</stEvt:when>
                        <stEvt:softwareAgent>Python Script</stEvt:softwareAgent>
                    </rdf:li>
                </rdf:Seq>
            </xmpMM:History>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Define the file path
file_path = './tmp/example.xmp'

# Write the XMP content to a file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file created at: {file_path}")
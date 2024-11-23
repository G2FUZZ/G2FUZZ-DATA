import os
from lxml import etree

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the XMP template
xmp_template = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c015 81.157285, 2014/12/12-00:43:15        ">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
            xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"
            xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#">
            <dc:format>image/jpeg</dc:format>
            <xmp:CreateDate>2020-01-01T12:00:00</xmp:CreateDate>
            <xmp:ModifyDate>2020-01-02T12:00:00</xmp:ModifyDate>
            <xmp:MetadataDate>2020-01-03T12:00:00</xmp:MetadataDate>
            <photoshop:DateCreated>2020-01-01T12:00:00</photoshop:DateCreated>
            <xmpMM:History>
                <rdf:Seq>
                    <rdf:li rdf:parseType="Resource">
                        <stEvt:action>created</stEvt:action>
                        <stEvt:instanceID>xmp.iid:123456</stEvt:instanceID>
                        <stEvt:when>2020-01-01T12:00:00</stEvt:when>
                        <stEvt:softwareAgent>Adobe Photoshop 21.0 (Windows)</stEvt:softwareAgent>
                        <stEvt:changed>/</stEvt:changed>
                    </rdf:li>
                </rdf:Seq>
            </xmpMM:History>
            <dc:description>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Flexibility: XMP is designed to be flexible and adaptive to various use cases, from simple tagging with basic information to complex metadata structures for archiving and rights management.</rdf:li>
                </rdf:Alt>
            </dc:description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

# Parse the XMP template
xmp_root = etree.fromstring(xmp_template)

# Save the XMP content to a file
xmp_file_path = './tmp/metadata.xmp'
with open(xmp_file_path, 'wb') as xmp_file:
    xmp_file.write(etree.tostring(xmp_root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

print(f'XMP file saved to {xmp_file_path}')
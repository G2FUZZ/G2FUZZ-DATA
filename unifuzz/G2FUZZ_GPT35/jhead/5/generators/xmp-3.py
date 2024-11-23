import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate XMP file
xmp_content = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
            xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"
            xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#"
            xmp:CreatorTool="Python"
            xmpMM:DocumentID="uuid:1234567890"
            xmpMM:InstanceID="uuid:0987654321"
            xmpMM:OriginalDocumentID="uuid:abcdef123456"
            xmpMM:RenditionClass="proof:pdf"
            xmpMM:VersionID="1.0"/>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

file_name = 'standardized_file.xmp'
file_path = os.path.join(directory, file_name)

with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file '{file_name}' generated and saved in '{directory}'")
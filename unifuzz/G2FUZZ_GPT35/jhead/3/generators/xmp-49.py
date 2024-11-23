import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp files with more complex file features
num_files = 5

for i in range(1, num_files + 1):
    filename = f"./tmp/file_{i}.xmp"
    with open(filename, 'w') as file:
        file.write(f"""<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
        <x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c067 79.157747, 2015/03/30-23:40:42">
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
                <rdf:Description rdf:about=""
                    xmlns:dc="http://purl.org/dc/elements/1.1/"
                    xmlns:xmp="http://ns.adobe.com/xap/1.0/"
                    xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
                    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
                    xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"
                    xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#">
                    <dc:title>File {i}</dc:title>
                    <dc:description>This is a more complex XMP file with extended metadata</dc:description>
                    <dc:creator>John Doe</dc:creator>
                    <dc:date>2022-01-01</dc:date>
                    <dc:format>application/pdf</dc:format>
                    <dc:language>en-US</dc:language>
                    <xmp:Rating>5</xmp:Rating>
                    <xmpMM:DocumentID>uuid:1234567890</xmpMM:DocumentID>
                    <xmpRights:Marked>True</xmpRights:Marked>
                    <stEvt:action>created</stEvt:action>
                    <stEvt:instanceID>uuid:abcdef1234567890</stEvt:instanceID>
                    <custom:CustomField1>Custom Value 1</custom:CustomField1>
                    <custom:CustomField2>Custom Value 2</custom:CustomField2>
                    <custom:CustomNestedElement>
                        <custom:NestedField1>Nested Value 1</custom:NestedField1>
                        <custom:NestedField2>Nested Value 2</custom:NestedField2>
                    </custom:CustomNestedElement>
                </rdf:Description>
            </rdf:RDF>
        </x:xmpmeta>
        <?xpacket end='w'?>""")
    
print(f"{num_files} xmp files with more complex file features generated and saved in './tmp/' directory.")
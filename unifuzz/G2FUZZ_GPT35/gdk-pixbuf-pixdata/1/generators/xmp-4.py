import os

# Define the content for the xmp files
xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c140 79.160451, 2017/05/06-01:08:21">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:xmp="http://ns.adobe.com/xap/1.0/"
            xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
            xmlns:mp="http://www.microsoft.com/XMP/1.0"
            xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
            xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"
            xmlns:xmpGImg="http://ns.adobe.com/xap/1.0/g/img/"
            xmlns:xmpG="http://ns.adobe.com/xap/1.0/g/"
            xmlns:xmpNote="http://ns.adobe.com/xmp/note/"
            xmlns:xmpTPg="http://ns.adobe.com/xap/1.0/t/pg/"
            xmlns:pdf="http://ns.adobe.com/pdf/1.3/"
            xmlns:pdfx="http://ns.adobe.com/pdfx/1.3/"
            xmlns:pdfxid="http://www.npes.org/pdfx/ns/id/"
            xmlns:pdfxid="http://www.npes.org/pdfxid/1.3/"
            xmlns:pdfaid="http://www.aiim.org/pdfa/ns/id/"
            xmlns:pdfaid="http://www.aiim.org/pdfaid/1.3/"
            xmlns:ai="http://ns.adobe.com/ai/1.0/"
            xmlns:xmpGImg="http://ns.adobe.com/xap/1.0/g/img/"
            xmlns:xmpG="http://ns.adobe.com/xap/1.0/g/"
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:wc="http://ns.adobe.com/workingcopy/1.0/"
            xmlns:adobeBridge="http://ns.adobe.com/adobebridge/1.0/"
            xmlns:xapMM="http://ns.adobe.com/xap/1.0/mm/"
            xmlns:xmpG="http://ns.adobe.com/xap/1.0/g/"
            xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#">
            <dc:format>application/pdf</dc:format>
            <dc:creator>
                <rdf:Seq>
                    <rdf:li>John Doe</rdf:li>
                </rdf:Seq>
            </dc:creator>
            <dc:title>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Sample Document</rdf:li>
                </rdf:Alt>
            </dc:title>
            <dc:description>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Sample description with Unicode characters: 你好, Hello, привет</rdf:li>
                </rdf:Alt>
            </dc:description>
            <dc:publisher>
                <rdf:Bag>
                    <rdf:li>My Publisher</rdf:li>
                </rdf:Bag>
            </dc:publisher>
            <xmp:CreateDate>2019-03-25T10:30:00Z</xmp:CreateDate>
            <xmp:MetadataDate>2019-03-25T10:30:00Z</xmp:MetadataDate>
            <xmp:ModifyDate>2019-03-25T10:30:00Z</xmp:ModifyDate>
            <xmp:Rating>5</xmp:Rating>
            <xmp:Identifier>
                <rdf:Bag>
                    <rdf:li>uuid:1234567890</rdf:li>
                </rdf:Bag>
            </xmp:Identifier>
            <mp:logicalFileName>sample.pdf</mp:logicalFileName>
            <mp:physicalFileName>sample.pdf</mp:physicalFileName>
            <xmpMM:DocumentID>uuid:1234567890</xmpMM:DocumentID>
            <xmpMM:InstanceID>uuid:1234567891</xmpMM:InstanceID>
            <xmpMM:RenditionClass>default</xmpMM:RenditionClass>
            <xmpMM:VersionID>1</xmpMM:VersionID>
            <xmpMM:History>
                <rdf:Seq>
                    <rdf:li>
                        <rdf:Description rdf:about="">
                            <stEvt:action>created</stEvt:action>
                            <stEvt:when>2019-03-25T10:30:00Z</stEvt:when>
                            <stEvt:softwareAgent>Adobe InDesign CC 14.0</stEvt:softwareAgent>
                        </rdf:Description>
                    </rdf:li>
                </rdf:Seq>
            </xmpMM:History>
            <xmpMM:Ingredients>
                <rdf:Bag>
                    <rdf:li>ingredient1</rdf:li>
                    <rdf:li>ingredient2</rdf:li>
                </rdf:Bag>
            </xmpMM:Ingredients>
            <xmpMM:Ingredients>
                <rdf:Bag>
                    <rdf:li>ingredient3</rdf:li>
                    <rdf:li>ingredient4</rdf:li>
                </rdf:Bag>
            </xmpMM:Ingredients>
            <xmpMM:Ingredients>
                <rdf:Bag>
                    <rdf:li>ingredient5</rdf:li>
                </rdf:Bag>
            </xmpMM:Ingredients>
            <xmpMM:Manifest>
                <rdf:Bag>
                    <rdf:li>manifest1</rdf:li>
                    <rdf:li>manifest2</rdf:li>
                </rdf:Bag>
            </xmpMM:Manifest>
            <xmpMM:Manifest>
                <rdf:Bag>
                    <rdf:li>manifest3</rdf:li>
                    <rdf:li>manifest4</rdf:li>
                </rdf:Bag>
            </xmpMM:Manifest>
            <xmpMM:Manifest>
                <rdf:Bag>
                    <rdf:li>manifest5</rdf:li>
                </rdf:Bag>
            </xmpMM:Manifest>
            <xmpMM:DocumentParts>
                <rdf:Bag>
                    <rdf:li>part1</rdf:li>
                    <rdf:li>part2</rdf:li>
                </rdf:Bag>
            </xmpMM:DocumentParts>
            <xmpMM:DocumentParts>
                <rdf:Bag>
                    <rdf:li>part3</rdf:li>
                    <rdf:li>part4</rdf:li>
                </rdf:Bag>
            </xmpMM:DocumentParts>
            <xmpMM:DocumentParts>
                <rdf:Bag>
                    <rdf:li>part5</rdf:li>
                </rdf:Bag>
            </xmpMM:DocumentParts>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the generated xmp files
for i in range(5):
    with open(f'./tmp/file_{i}.xmp', 'w') as f:
        f.write(xmp_content)

print("XMP files generated and saved successfully!")
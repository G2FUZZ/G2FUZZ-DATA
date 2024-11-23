import os
import datetime

metadata = {
    "Author": "John Doe",
    "Copyright": "2022",
    "Keywords": ["Python", "XMP", "Metadata"],
    "CreationDate": datetime.datetime.now().strftime("%Y-%m-%d")
}

xmp_template = """<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:creator>{Author}</dc:creator>
            <dc:rights>{Copyright}</dc:rights>
            <dc:subject>
                <rdf:Bag>
                    {Keywords}
                </rdf:Bag>
            </dc:subject>
            <dc:date>{CreationDate}</dc:date>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

for i in range(3):
    filename = f"./tmp/file_{i+1}.xmp"
    with open(filename, 'w') as f:
        keywords = "\n".join([f"<rdf:li>{keyword}</rdf:li>" for keyword in metadata["Keywords"]])
        xmp_content = xmp_template.format(Author=metadata["Author"], Copyright=metadata["Copyright"],
                                          Keywords=keywords, CreationDate=metadata["CreationDate"])
        f.write(xmp_content)

print("XMP files created successfully.")
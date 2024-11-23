import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP files with embedded thumbnails
for i in range(3):
    xmp_content = f"""
    <?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
    <x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Adobe XMP Core 5.4-c005 80.25, 2016/09/16-03:31:08'>
        <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
            <rdf:Description rdf:about=''
                xmlns:dc='http://purl.org/dc/elements/1.1/'>
                <dc:title>
                    <rdf:Alt>
                        <rdf:li xml:lang='x-default'>Embedded Thumbnail {i+1}</rdf:li>
                    </rdf:Alt>
                </dc:title>
                <dc:description>
                    <rdf:Alt>
                        <rdf:li xml:lang='x-default'>This is an embedded thumbnail for preview</rdf:li>
                    </rdf:Alt>
                </dc:description>
                <dc:format>image/jpeg</dc:format>
            </rdf:Description>
        </rdf:RDF>
    </x:xmpmeta>
    <?xpacket end='w'?>
    """
    with open(f'./tmp/embedded_thumbnail_{i+1}.xmp', 'w') as file:
        file.write(xmp_content)
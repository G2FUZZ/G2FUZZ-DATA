import os

# Create a directory to store generated xmp files
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP files with more complex file structures
xmp_data_complex = """
<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='XMP Core 4.4.0'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about=''
            xmlns:dc='http://purl.org/dc/elements/1.1/'
            xmlns:photoshop='http://ns.adobe.com/photoshop/1.0/'>
            <dc:title>Sample Title</dc:title>
            <dc:creator>
                <rdf:Seq>
                    <rdf:li>John Doe</rdf:li>
                    <rdf:li>Jane Smith</rdf:li>
                </rdf:Seq>
            </dc:creator>
            <photoshop:Country>USA</photoshop:Country>
            <photoshop:Keywords>
                <rdf:Bag>
                    <rdf:li>Landscape</rdf:li>
                    <rdf:li>Nature</rdf:li>
                </rdf:Bag>
            </photoshop:Keywords>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

file_path_complex = './tmp/extended_xmp_complex.xmp'

with open(file_path_complex, 'w') as f:
    f.write(xmp_data_complex)

print(f"Extended XMP file generated at: {file_path_complex}")
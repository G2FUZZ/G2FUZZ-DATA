import os

# Create a directory to store generated XMP files
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP files with additional complex features
xmp_data = """
<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='XMP Core 4.4.0'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about=''
            xmlns:dc='http://purl.org/dc/elements/1.1/'
            xmlns:exif='http://ns.adobe.com/exif/1.0/'
            xmlns:xmp='http://ns.adobe.com/xap/1.0/'
            xmlns:photoshop='http://ns.adobe.com/photoshop/1.0/'>
            <dc:format>image/jpeg</dc:format>
            <dc:format>image/tiff</dc:format>
            <exif:Make>Canon</exif:Make>
            <exif:Model>EOS 5D Mark IV</exif:Model>
            <xmp:CreatorTool>Adobe Photoshop CC</xmp:CreatorTool>
            <photoshop:ColorMode>RGB Color</photoshop:ColorMode>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
"""

file_path = './tmp/extended_xmp.xmp'

with open(file_path, 'w') as f:
    f.write(xmp_data)

print(f"Extended XMP file generated at: {file_path}")
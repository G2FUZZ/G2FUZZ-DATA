import os

# Generate the XMP file content
xmp_content = '''<?xml version="1.0" encoding="UTF-8"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c132 79.159768, 2019/04/02-00:03:29">
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
        <rdf:Description rdf:about=""
            xmlns:dc="http://purl.org/dc/elements/1.1/">
            <dc:format>application/pdf</dc:format>
            <dc:title>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">Sample XMP File</rdf:li>
                </rdf:Alt>
            </dc:title>
            <dc:description>
                <rdf:Alt>
                    <rdf:li xml:lang="x-default">This is a sample XMP file generated using Python.</rdf:li>
                </rdf:Alt>
            </dc:description>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>'''

# Create the tmp directory if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the XMP file into the tmp directory
file_path = './tmp/sample.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f'XMP file generated and saved at: {file_path}')
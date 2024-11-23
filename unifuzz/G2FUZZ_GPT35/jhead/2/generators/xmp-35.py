import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate xmp files with additional complex file features
num_files = 5

for i in range(num_files):
    filename = f'{directory}/file_{i}.xmp'
    with open(filename, 'w') as file:
        file.write(f'''
        <x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 5.0.0">
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
                <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">
                    <dc:title>Image Version {i+1}</dc:title>
                    <dc:description>Full metadata for Image Version {i+1}</dc:description>
                    <dc:creator>John Doe</dc:creator>
                    <dc:rights>Copyright © 2022 John Doe. All rights reserved.</dc:rights>
                </rdf:Description>
            </rdf:RDF>
        </x:xmpmeta>
        ''')
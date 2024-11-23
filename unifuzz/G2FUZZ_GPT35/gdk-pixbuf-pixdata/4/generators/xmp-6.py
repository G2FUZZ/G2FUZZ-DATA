import os

# Create tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate xmp files with linked resources
for i in range(3):  # Generate 3 xmp files
    file_content = f"""
    <?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
    <x:xmpmeta xmlns:x='adobe:ns:meta/'>
        <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
            <rdf:Description rdf:about=''>
                <xmp:LinkedResources>
                    <rdf:Bag>
                        <rdf:li>
                            <rdf:Description>
                                <xmp:ResourceRef>http://example.com/resource{i}</xmp:ResourceRef>
                            </rdf:Description>
                        </rdf:li>
                    </rdf:Bag>
                </xmp:LinkedResources>
            </rdf:Description>
        </rdf:RDF>
    </x:xmpmeta>
    <?xpacket end='w'?>
    """

    with open(f'./tmp/file_{i}.xmp', 'w') as f:
        f.write(file_content)

print("XMP files generated successfully.")
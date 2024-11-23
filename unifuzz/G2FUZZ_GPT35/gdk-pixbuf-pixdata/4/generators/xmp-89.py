import os

# Create tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate xmp files with linked resources and additional features
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
                                <xmp:ResourceName>Resource{i}_Name</xmp:ResourceName>
                                <xmp:ResourceType>Image</xmp:ResourceType>
                                <xmp:ResourceSize>1024 KB</xmp:ResourceSize>
                                <xmp:ResourceDescription>This is Resource{i}</xmp:ResourceDescription>
                            </rdf:Description>
                        </rdf:li>
                        <rdf:li>
                            <rdf:Description>
                                <xmp:ResourceRef>http://example.com/resource{i}_alt</xmp:ResourceRef>
                                <xmp:ResourceName>Resource{i}_Alt_Name</xmp:ResourceName>
                                <xmp:ResourceType>Video</xmp:ResourceType>
                                <xmp:ResourceSize>2048 KB</xmp:ResourceSize>
                                <xmp:ResourceDescription>This is an alternate Resource{i}</xmp:ResourceDescription>
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

print("XMP files with additional complex file features generated successfully.")
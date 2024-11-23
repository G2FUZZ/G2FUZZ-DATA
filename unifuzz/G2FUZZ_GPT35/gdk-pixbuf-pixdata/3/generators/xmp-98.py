import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate XMP file with advanced hierarchical structure and properties
xmp_content = '''<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/'>
    <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
        <rdf:Description rdf:about='' xmlns:xmp='http://ns.adobe.com/xap/1.0/'
            xmlns:custom='http://example.com/custom/'>
            <xmp:HierarchicalStructure>
                <xmp:ComplexRelationship>
                    <xmp:Property1>Value1</xmp:Property1>
                    <xmp:Property2>Value2</xmp:Property2>
                    <custom:CustomProperty>CustomValue</custom:CustomProperty>
                </xmp:ComplexRelationship>
                <xmp:NestedStructure>
                    <xmp:SubProperty>SubValue</xmp:SubProperty>
                </xmp:NestedStructure>
            </xmp:HierarchicalStructure>
        </rdf:Description>
    </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>
'''

file_path = './tmp/advanced_example.xmp'
with open(file_path, 'w') as file:
    file.write(xmp_content)
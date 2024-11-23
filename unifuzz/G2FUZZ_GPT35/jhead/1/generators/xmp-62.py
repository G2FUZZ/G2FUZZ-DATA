import os

xmp_content = """
<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
      <rdf:Description rdf:about=""
            xmlns:xmp="http://ns.adobe.com/xap/1.0/">
         <xmp:Rating>5</xmp:Rating>
         <xmp:CreateDate>2022-01-01</xmp:CreateDate>
         <xmp:Embeddable>true</xmp:Embeddable>
         <xmp:CustomNestedElement>
            <xmp:CustomAttribute1>Attribute1</xmp:CustomAttribute1>
            <xmp:CustomAttribute2>Attribute2</xmp:CustomAttribute2>
         </xmp:CustomNestedElement>
      </rdf:Description>
      <rdf:Description rdf:about=""
            xmlns:custom="http://example.com/custom/">
         <custom:CustomProperty1>Value1</custom:CustomProperty1>
         <custom:CustomProperty2>Value2</custom:CustomProperty2>
         <custom:CustomNestedElement>
            <custom:CustomNestedAttribute1>NestedAttribute1</custom:CustomNestedAttribute1>
            <custom:CustomNestedAttribute2>NestedAttribute2</custom:CustomNestedAttribute2>
         </custom:CustomNestedElement>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

with open('./tmp/sample_file_extended.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file with more complex file structures generated successfully.")
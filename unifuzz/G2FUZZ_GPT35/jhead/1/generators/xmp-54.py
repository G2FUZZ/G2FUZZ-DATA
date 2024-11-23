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
         <xmp:CustomField1>Value1</xmp:CustomField1>
         <xmp:CustomField2>Value2</xmp:CustomField2>
         <rdf:Bag>
            <rdf:li>Item 1</rdf:li>
            <rdf:li>Item 2</rdf:li>
         </rdf:Bag>
         <rdf:Description rdf:about="ChildNode1">
            <xmp:ChildField1>ChildValue1</xmp:ChildField1>
         </rdf:Description>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
"""

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

with open('./tmp/sample_file.xmp', 'w') as file:
    file.write(xmp_content)

print("XMP file with complex file structures generated successfully.")
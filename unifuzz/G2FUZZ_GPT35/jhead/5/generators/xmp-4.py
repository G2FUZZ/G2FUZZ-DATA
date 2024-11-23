import os

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the xmp file with the required features
xmp_content = """
<XMPMetadata xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c132 79.159624, 2019/12/12-00:43:15">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
      xmlns:xmp="http://ns.adobe.com/xap/1.0/"
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
      xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
      xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"
      xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#"
      xmp:CreatorTool="Adobe Photoshop Lightroom Classic 9.2 (Windows)"
      dc:format="image/jpeg"
      photoshop:ColorMode="3"
      xmpMM:OriginalDocumentID="A29D3F0A6147A12B6E6D7A1475E6CFD7"
      xmpMM:DocumentID="xmp.id:0a5a2b8e-5c3a-4c30-aeb3-12a4b0975a1a"
      xmpMM:InstanceID="xmp.iid:0a5a2b8e-5c3a-4c30-aeb3-12a4b0975a1a"
      xmpMM:DerivedFrom
        <rdf:Bag>
          <rdf:li
            stEvt:action="converted"
            stEvt:parameters="from image/tiff to image/jpeg"
            stEvt:instanceID="xmp.iid:0a5a2b8e-5c3a-4c30-aeb3-12a4b0975a1a"
            stEvt:softwareAgent="Adobe Photoshop Lightroom Classic 9.2 (Windows)"
            stEvt:when="2020-04-19T17:23:46-07:00"
            stRef:documentID="xmp.id:0a5a2b8e-5c3a-4c30-aeb3-12a4b0975a1a"/>
        </rdf:Bag>
      <xmpMM:History>
        <rdf:Seq>
          <rdf:li
            stEvt:action="saved"
            stEvt:instanceID="xmp.iid:0a5a2b8e-5c3a-4c30-aeb3-12a4b0975a1a"
            stEvt:when="2020-04-19T17:23:46-07:00"
            stEvt:softwareAgent="Adobe Photoshop Lightroom Classic 9.2 (Windows)"
            stEvt:changed="/"
            stEvt:parameters="from image/tiff to image/jpeg"/>
        </rdf:Seq>
      </xmpMM:History>
    </rdf:Description>
  </rdf:RDF>
</XMPMetadata>
"""

# Save the xmp file
with open('./tmp/metadata.xmp', 'w') as f:
    f.write(xmp_content)

print("XMP file generated and saved successfully.")
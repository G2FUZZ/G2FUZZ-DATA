import os

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the XMP file with even more complex file structures and additional custom metadata
xmp_content = """
<XMPMetadata xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c132 79.159624, 2019/12/12-00:43:15">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
      xmlns:xmp="http://ns.adobe.com/xap/1.0/"
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:custom="http://example.com/custom/"
      xmp:Rating="5"
      dc:creator="John Doe"
      custom:CustomMetadata
        <rdf:Bag>
          <rdf:li>
            <custom:Feature3>Value3</custom:Feature3>
            <custom:Feature4>Value4</custom:Feature4>
            <custom:FeatureArray>
              <rdf:Seq>
                <rdf:li>ArrayValue1</rdf:li>
                <rdf:li>ArrayValue2</rdf:li>
                <rdf:li>ArrayValue3</rdf:li>
              </rdf:Seq>
            </custom:FeatureArray>
          </rdf:li>
          <rdf:li>
            <custom:Feature5>Value5</custom:Feature5>
            <custom:Feature6>Value6</custom:Feature6>
            <custom:FeatureArray>
              <rdf:Seq>
                <rdf:li>ArrayValue4</rdf:li>
                <rdf:li>ArrayValue5</rdf:li>
                <rdf:li>ArrayValue6</rdf:li>
              </rdf:Seq>
            </custom:FeatureArray>
          </rdf:li>
        </rdf:Bag>
    </rdf:Description>
  </rdf:RDF>
</XMPMetadata>
"""

# Save the XMP file
with open('./tmp/extended_metadata_v3.xmp', 'w') as f:
    f.write(xmp_content)

print("Extended XMP file v3 generated and saved successfully.")
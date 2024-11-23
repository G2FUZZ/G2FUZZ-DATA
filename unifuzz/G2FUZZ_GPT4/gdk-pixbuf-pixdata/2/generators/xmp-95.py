import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the XMP file with more complex structures
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.6-c015 81.157285, 2014/12/12-00:43:15        ">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/">
   <dc:description>
    Synchronization of Metadata: XMP facilitates the synchronization of metadata among different files, ensuring consistency across documents, images, and other media types.
   </dc:description>
   <dc:creator>
    <rdf:Seq>
     <rdf:li>Creator Name</rdf:li>
     <rdf:li>Second Creator</rdf:li>
    </rdf:Seq>
   </dc:creator>
   <dc:title>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">Sample Title</rdf:li>
    </rdf:Alt>
   </dc:title>
  </rdf:Description>
  <rdf:Description rdf:about=""
    xmlns:exif="http://ns.adobe.com/exif/1.0/">
   <exif:DateTimeOriginal>2023-01-01T12:00:00</exif:DateTimeOriginal>
   <exif:UserComment>An example comment here.</exif:UserComment>
  </rdf:Description>
  <rdf:Description rdf:about=""
    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/">
   <photoshop:Headline>Sample Headline</photoshop:Headline>
   <photoshop:Credit>Photographer's Name</photoshop:Credit>
  </rdf:Description>
  <rdf:Description rdf:about=""
    xmlns:xmp="http://ns.adobe.com/xap/1.0/">
   <xmp:Rating>5</xmp:Rating>
  </rdf:Description>
  <rdf:Description rdf:about=""
    xmlns:camera="http://ns.adobe.com/camera/1.0/">
   <camera:model>Camera Model Name</camera:model>
   <camera:lens>Lens Model</camera:lens>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>
'''

# Define the file path
file_path = './tmp/complex_feature_description.xmp'

# Write the content to the XMP file
with open(file_path, 'w') as file:
    file.write(xmp_content)

print(f"XMP file generated at: {file:}")
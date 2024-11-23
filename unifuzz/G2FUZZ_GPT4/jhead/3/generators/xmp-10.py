import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# XMP content focusing on Licensing and Rights Management
xmp_content = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
   <xmpRights:UsageTerms>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">This content is protected under copyright law and can only be used under specific licensing terms and conditions.</rdf:li>
    </rdf:Alt>
   </xmpRights:UsageTerms>
   <xmpRights:WebStatement>http://example.com/rights_statement</xmpRights:WebStatement>
   <xmpRights:Marked>True</xmpRights:Marked>
   <xmpRights:Owner>http://example.com/owner_profile</xmpRights:Owner>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# File path
file_path = './tmp/licensing_rights.xmp'

# Writing the XMP content to a file
with open(file_path, 'w') as f:
    f.write(xmp_content)

print(f'XMP file created at {file_path}')
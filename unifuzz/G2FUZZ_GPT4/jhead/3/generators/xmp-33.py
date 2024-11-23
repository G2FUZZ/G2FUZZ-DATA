import os
from datetime import datetime

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# XMP content with complex features including multiple languages, custom license, creator, and creation date
xmp_template = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:xmp="http://ns.adobe.com/xap/1.0/">
   <xmpRights:UsageTerms>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{usage_terms_default}</rdf:li>
     <rdf:li xml:lang="en-us">{usage_terms_en_us}</rdf:li>
     <rdf:li xml:lang="es">{usage_terms_es}</rdf:li>
    </rdf:Alt>
   </xmpRights:UsageTerms>
   <xmpRights:WebStatement>{web_statement}</xmpRights:WebStatement>
   <xmpRights:Marked>True</xmpRights:Marked>
   <xmpRights:Owner>{owner}</xmpRights:Owner>
   <dc:creator>
    <rdf:Seq>
     <rdf:li>{creator}</rdf:li>
    </rdf:Seq>
   </dc:creator>
   <xmp:CreateDate>{create_date}</xmp:CreateDate>
   <xmpRights:License>{license}</xmpRights:License>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Customizable fields
usage_terms_default = "This content is protected under copyright law and can only be used under specific licensing terms and conditions."
usage_terms_en_us = "This content is copyrighted and must be used according to licensing terms."
usage_terms_es = "Este contenido está protegido por leyes de derechos de autor y solo puede utilizarse según los términos y condiciones de la licencia."
web_statement = "http://example.com/rights_statement"
owner = "http://example.com/owner_profile"
creator = "John Doe"
create_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
license = "Custom License: This content is licensed under specific terms that allow for personal and educational use only."

xmp_content = xmp_template.format(usage_terms_default=usage_terms_default, usage_terms_en_us=usage_terms_en_us, usage_terms_es=usage_terms_es, web_statement=web_statement, owner=owner, creator=creator, create_date=create_date, license=license)

# File path
file_path = './tmp/complex_licensing_rights.xmp'

# Writing the XMP content to a file
with open(file_path, 'w') as f:
    f.write(xmp_content)

print(f'XMP file created at {file_path}')
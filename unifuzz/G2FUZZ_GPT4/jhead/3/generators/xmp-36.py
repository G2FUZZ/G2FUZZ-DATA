import os
from datetime import datetime

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Extended XMP content with complex features including multiple languages, multiple creators, contributors, camera information, and rights for multiple countries
xmp_template = '''<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:xmp="http://ns.adobe.com/xap/1.0/"
    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
    xmlns:Iptc4xmpCore="http://iptc.org/std/Iptc4xmpCore/1.0/xmlns/"
    xmlns:tiff="http://ns.adobe.com/tiff/1.0/"
    xmlns:exif="http://ns.adobe.com/exif/1.0/">
   <xmpRights:UsageTerms>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{usage_terms_default}</rdf:li>
     <rdf:li xml:lang="en-us">{usage_terms_en_us}</rdf:li>
     <rdf:li xml:lang="es">{usage_terms_es}</rdf:li>
    </rdf:Alt>
   </xmpRights:UsageTerms>
   <xmpRights:WebStatement>{web_statement}</xmpRights:WebStatement>
   <xmpRights:Marked>True</xmpRights:Marked>
   <xmpRights:Owner>
    <rdf:Bag>
     <rdf:li>{owner}</rdf:li>
    </rdf:Bag>
   </xmpRights:Owner>
   <dc:creator>
    <rdf:Seq>
     {creators}
    </rdf:Seq>
   </dc:creator>
   <dc:description>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">{description_default}</rdf:li>
     <rdf:li xml:lang="en">{description_en}</rdf:li>
     <rdf:li xml:lang="fr">{description_fr}</rdf:li>
    </rdf:Alt>
   </dc:description>
   <xmp:CreateDate>{create_date}</xmp:CreateDate>
   <xmpRights:License>{license}</xmpRights:License>
   <dc:contributor>
    <rdf:Seq>
     {contributors}
    </rdf:Seq>
   </dc:contributor>
   <photoshop:Credit>{credit}</photoshop:Credit>
   <Iptc4xmpCore:CountryCode>{country_code}</Iptc4xmpCore:CountryCode>
   <tiff:Make>{camera_make}</tiff:Make>
   <tiff:Model>{camera_model}</tiff:Model>
   <exif:ISOSpeedRatings>{iso_speed}</exif:ISOSpeedRatings>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''

# Customizable fields with more complex structures
creators = '\n     '.join([f'<rdf:li>{creator}</rdf:li>' for creator in ["John Doe", "Jane Doe"]])
contributors = '\n     '.join([f'<rdf:li>{contributor}</rdf:li>' for contributor in ["Editor One", "Editor Two"]])
description_default = "An extended example of XMP data embedding."
description_en = "This is an extended example of XMP data, including detailed metadata."
description_fr = "Ceci est un exemple étendu de données XMP, incluant des métadonnées détaillées."

# Other metadata fields
usage_terms_default = "This content is protected under copyright law and can only be used under specific licensing terms and conditions."
usage_terms_en_us = "This content is copyrighted and must be used according to licensing terms."
usage_terms_es = "Este contenido está protegido por leyes de derechos de autor y solo puede utilizarse según los términos y condiciones de la licencia."
web_statement = "http://example.com/rights_statement"
owner = "http://example.com/owner_profile"
create_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
license = "Custom License: This content is licensed under specific terms that allow for personal and educational use only."
credit = "Photography Studio XYZ"
country_code = "US"
camera_make = "Nikon"
camera_model = "D850"
iso_speed = "64"

xmp_content = xmp_template.format(usage_terms_default=usage_terms_default, usage_terms_en_us=usage_terms_en_us, usage_terms_es=usage_terms_es, web_statement=web_statement, owner=owner, creators=creators, description_default=description_default, description_en=description_en, description_fr=description_fr, create_date=create_date, license=license, contributors=contributors, credit=credit, country_code=country_code, camera_make=camera_make, camera_model=camera_model, iso_speed=iso_speed)

# File path
file_path = './tmp/extended_complex_licensing_rights.xmp'

# Writing the XMP content to a file
with open(file_path, 'w') as f:
    f.write(xmp_content)

print(f'Extended XMP file created at {file_path}')
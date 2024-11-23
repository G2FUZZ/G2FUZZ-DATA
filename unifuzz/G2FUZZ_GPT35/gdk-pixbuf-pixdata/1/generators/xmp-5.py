import os

def generate_xmp_file(version, output_dir):
    xmp_content = f"""<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Adobe XMP Core 5.6-c140 79.160451, 2015/09/29-01:07:23        '>
   <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
      <rdf:Description rdf:about=''
            xmlns:xmp='http://ns.adobe.com/xap/1.0/'>
         <xmp:ModifyDate>2022-10-05T12:00:00</xmp:ModifyDate>
         <xmp:Version>{version}</xmp:Version>
      </rdf:Description>
   </rdf:RDF>
</x:xmpmeta>
<?xpacket end='w'?>"""

    file_name = f"xmp_version_{version}.xmp"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, 'w') as file:
        file.write(xmp_content)

output_directory = './tmp/'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

version = "Latest"

generate_xmp_file(version, output_directory)
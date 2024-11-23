from lxml import etree
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the output paths
output_video_path = os.path.join(output_dir, "example_streaming_with_dirac.mp4")
output_didl_path = os.path.join(output_dir, "example_streaming_with_dirac_didl.xml")

# Define the namespace
NSMAP = {'didl': 'urn:mpeg:mpeg21:2002:02-DIDL-NS'}
# Generate MPEG-21 Part 2 DIDL file
didl = etree.Element("{urn:mpeg:mpeg21:2002:02-DIDL-NS}Didl", nsmap=NSMAP)
item = etree.SubElement(didl, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Item", nsmap=NSMAP)
component = etree.SubElement(item, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Component", nsmap=NSMAP)
resource = etree.SubElement(component, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Resource", ref=output_video_path, nsmap=NSMAP)
descriptor = etree.SubElement(resource, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Descriptor", nsmap=NSMAP)

# Descriptor for existing features
statement_existing = etree.SubElement(descriptor, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Statement", nsmap=NSMAP)
statement_existing.text = "This is an example of MPEG-21 DIDL for a streaming video."

# Descriptor for Dirac Video Codec feature
descriptor_dirac = etree.SubElement(resource, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Descriptor", nsmap=NSMAP)
statement_dirac = etree.SubElement(descriptor_dirac, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Statement", nsmap=NSMAP)
statement_dirac.text = "4. **Dirac Video Codec**: MP4 can encapsulate video streams encoded with the Dirac codec, an open and royalty-free video compression format that competes with H.264."

# Pretty print and write DIDL XML
didl_string = etree.tostring(didl, pretty_print=True, xml_declaration=True, encoding="UTF-8")
with open(output_didl_path, "wb") as xml_file:
    xml_file.write(didl_string)
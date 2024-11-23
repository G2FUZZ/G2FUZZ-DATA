from lxml import etree
import os

# Ensure the tmp directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Define the output paths
output_video_path = os.path.join(output_dir, "example_streaming.mp4")
output_didl_path = os.path.join(output_dir, "example_streaming_didl.xml")

# Define the namespace
NSMAP = {'didl': 'urn:mpeg:mpeg21:2002:02-DIDL-NS'}
# Generate MPEG-21 Part 2 DIDL file
didl = etree.Element("{urn:mpeg:mpeg21:2002:02-DIDL-NS}Didl", nsmap=NSMAP)
item = etree.SubElement(didl, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Item", nsmap=NSMAP)
component = etree.SubElement(item, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Component", nsmap=NSMAP)
resource = etree.SubElement(component, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Resource", ref=output_video_path, nsmap=NSMAP)

# Adding Progressive Download feature
descriptor_pd = etree.SubElement(resource, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Descriptor", nsmap=NSMAP)
statement_pd = etree.SubElement(descriptor_pd, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Statement", nsmap=NSMAP)
statement_pd.text = "Progressive Download: MP4 files support progressive download, enabling playback to start before the file is completely downloaded, enhancing user experience on slower connections."

# Original Descriptor for example
descriptor = etree.SubElement(resource, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Descriptor", nsmap=NSMAP)
statement = etree.SubElement(descriptor, "{urn:mpeg:mpeg21:2002:02-DIDL-NS}Statement", nsmap=NSMAP)
statement.text = "This is an example of MPEG-21 DIDL for a streaming video."

# Pretty print and write DIDL XML
didl_string = etree.tostring(didl, pretty_print=True, xml_declaration=True, encoding="UTF-8")
with open(output_didl_path, "wb") as xml_file:
    xml_file.write(didl_string)
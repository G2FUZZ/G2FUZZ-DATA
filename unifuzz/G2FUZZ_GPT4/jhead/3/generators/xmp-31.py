import os
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to create an rdf:Seq element
def create_rdf_seq(parent, tag, elements):
    seq = SubElement(parent, f'{rdf_ns}Seq')
    for elem in elements:
        li = SubElement(seq, f'{rdf_ns}li')
        li.text = elem
    return seq

# Namespaces
rdf_ns = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
x_ns = "{adobe:ns:meta/}"
dc_ns = "{http://purl.org/dc/elements/1.1/}"
photoshop_ns = "{http://ns.adobe.com/photoshop/1.0/}"
xmp_ns = "{http://ns.adobe.com/xap/1.0/}"
exif_ns = "{http://ns.adobe.com/exif/1.0/}"
custom_ns = "{http://www.example.com/ns/}"

# Sample metadata for dynamic XMP content generation
asset_metadata = {
    "description": "A more complex example with dynamic content generation.",
    "creator": ["Creator One", "Creator Two"],
    "headline": "Dynamic Headline Example",
    "create_date": "2023-01-01T12:00:00",
    "exposure_time": "1/100",
    "f_number": "8.0",
    "iso": "200",
    "custom_fields": [
        {"name": "CustomField1", "value": "Custom Value 1"},
        {"name": "CustomField2", "value": "Custom Value 2", "include": False},  # Conditional inclusion
        {"name": "CustomField3", "value": "Custom Value 3"}
    ]
}

# Create the root element
xmpmeta = Element(f'{x_ns}xmpmeta')
rdf = SubElement(xmpmeta, f'{rdf_ns}RDF')
description = SubElement(rdf, f'{rdf_ns}Description', {
    f'{rdf_ns}about': "",
    f'{dc_ns}xmlns': "http://purl.org/dc/elements/1.1/",
    f'{photoshop_ns}xmlns': "http://ns.adobe.com/photoshop/1.0/",
    f'{xmp_ns}xmlns': "http://ns.adobe.com/xap/1.0/",
    f'{exif_ns}xmlns': "http://ns.adobe.com/exif/1.0/",
    f'{custom_ns}xmlns': "http://www.example.com/ns/",
})

# Add metadata fields dynamically
SubElement(description, f'{dc_ns}description').text = asset_metadata["description"]
create_rdf_seq(description, f'{dc_ns}creator', asset_metadata["creator"])
SubElement(description, f'{photoshop_ns}Headline').text = asset_metadata["headline"]
SubElement(description, f'{xmp_ns}CreateDate').text = asset_metadata["create_date"]
SubElement(description, f'{exif_ns}ExposureTime').text = asset_metadata["exposure_time"]
SubElement(description, f'{exif_ns}FNumber').text = asset_metadata["f_number"]
SubElement(description, f'{exif_ns}ISO').text = asset_metadata["iso"]

# Add custom fields with conditional logic
for field in asset_metadata["custom_fields"]:
    if field.get("include", True):  # Default to include if not specified
        SubElement(description, f'{custom_ns}{field["name"]}').text = field["value"]

# Convert to a pretty XML string
dom = parseString(tostring(xmpmeta))
xmp_content = dom.toprettyxml()

# Path to the XMP file to be created
xmp_file_path = './tmp/dynamic_complex_feature_description.xmp'

# Write the XMP content to the file
with open(xmp_file_path, 'w') as xmp_file:
    xmp_file.write(xmp_content)

print(f"XMP file created at {xmp_file_path}")
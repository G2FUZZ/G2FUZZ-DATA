import os

# Create a directory to store the generated mif files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mif file with hyperlinks
mif_content = """
Depth = 32;
Width = 8;
Address_radix = dec;
Data_radix = dec;

CONTENT BEGIN
[0..31] : 0;
END;
"""

# Add a hyperlink to the mif file
mif_content_with_hyperlink = mif_content + "\n\n[ExternalResource](https://www.example.com)"

# Save the mif files with and without hyperlinks
with open('./tmp/sample_mif_without_hyperlink.mif', 'w') as f:
    f.write(mif_content)

with open('./tmp/sample_mif_with_hyperlink.mif', 'w') as f:
    f.write(mif_content_with_hyperlink)
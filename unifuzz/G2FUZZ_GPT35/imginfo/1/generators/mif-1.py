import os

# Create a directory for saving the generated mif files
os.makedirs('./tmp/', exist_ok=True)

# Generate mif file with text formatting
mif_text = """
<text>
  <font style="bold">Heading</font>
  <size value="12">This is a heading</size>
  
  <font style="italic">Subheading</font>
  <size value="10">This is a subheading</size>
  
  <font color="red">Important Text</font>
  <size value="8">This is an important text in red color</size>
  
  <align type="center">Centered Text</align>
  <size value="8">This text is aligned to the center</size>
</text>
"""

# Save the generated mif file
with open('./tmp/text_formatting.mif', 'w') as file:
    file.write(mif_text)
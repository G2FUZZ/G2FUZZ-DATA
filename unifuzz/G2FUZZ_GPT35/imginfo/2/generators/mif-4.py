import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mif file with tags for defining fonts, styles, colors, page layout, graphics, and text content
mif_content = """
<document>
    <fonts>
        <font name="Arial" size="12"/>
        <font name="Times New Roman" size="14"/>
    </fonts>
    
    <styles>
        <style name="Heading" font="Arial" size="16" color="blue"/>
        <style name="Body" font="Times New Roman" size="12" color="black"/>
    </styles>
    
    <colors>
        <color name="red" value="#FF0000"/>
        <color name="green" value="#00FF00"/>
    </colors>
    
    <page_layout>
        <margin top="1" bottom="1" left="1" right="1"/>
        <orientation>landscape</orientation>
    </page_layout>
    
    <graphics>
        <image src="logo.png" width="200" height="100"/>
    </graphics>
    
    <text_content>
        <paragraph style="Heading">Introduction</paragraph>
        <paragraph style="Body">This is a sample text content.</paragraph>
    </text_content>
</document>
"""

with open('./tmp/sample.mif', 'w') as f:
    f.write(mif_content)

print("MIF file generated successfully.")
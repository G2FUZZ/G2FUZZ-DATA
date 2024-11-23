import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate mif file with text formatting information
text_formatting_data = '''
<text_formatting>
    <styles>
        <style name="Heading1" font="Arial" size="16" color="black" bold="True"/>
        <style name="BodyText" font="Times New Roman" size="12" color="black" bold="False"/>
    </styles>
</text_formatting>
'''

with open('./tmp/text_formatting.mif', 'w') as file:
    file.write(text_formatting_data)

print("mif file with text formatting information generated successfully.")
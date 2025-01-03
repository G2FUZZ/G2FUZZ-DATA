import os

# Create a directory if it does not exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate MIF file with text formatting features
mif_content = """
<MakerDocument>
    <MIFFile>
        <Title>
            Text Formatting Example
        </Title>
        <Body>
            <Para>
                <TextFont <Font Family='Arial' Weight='Bold' Size='12'>This text is bold</TextFont>
            </Para>
            <Para>
                <TextFont <Font Family='Times' Size='14'>This text is in Times font family</TextFont>
            </Para>
            <Para>
                <TextColor Color='red'>This text is in red color</TextColor>
            </Para>
            <Para>
                <TextAlign Alignment='center'>This text is center-aligned</TextAlign>
            </Para>
            <Para>
                <TextLeading Leading='2'>This text has leading of 2</TextLeading>
            </Para>
        </Body>
    </MIFFile>
</MakerDocument>
"""

# Save the generated MIF file
with open('./tmp/text_formatting_example.mif', 'w') as file:
    file.write(mif_content)

print("MIF file saved successfully.")
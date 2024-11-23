import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample MIF file with graphics and images instructions
mif_content = """
<MIFFile>
    <Graphics>
        <Image>
            <Name>example_image.png</Name>
            <Placement>
                <X>100</X>
                <Y>200</Y>
            </Placement>
            <Properties>
                <Width>300</Width>
                <Height>150</Height>
            </Properties>
        </Image>
    </Graphics>
</MIFFile>
"""

# Save the generated MIF file
with open('./tmp/sample.mif', 'w') as f:
    f.write(mif_content)

print("MIF file with graphics and images instructions generated and saved in './tmp/sample.mif'")
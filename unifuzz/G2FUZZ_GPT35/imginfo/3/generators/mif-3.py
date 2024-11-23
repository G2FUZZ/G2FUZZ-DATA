import os

# Create a directory to save the generated files if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate MIF file with page layout features
mif_content = """
<PageLayout>
    <Margins>
        <Top>1in</Top>
        <Bottom>1in</Bottom>
        <Left>0.75in</Left>
        <Right>0.75in</Right>
    </Margins>
    <Header>
        <Height>0.5in</Height>
    </Header>
    <Footer>
        <Height>0.5in</Height>
    </Footer>
    <PageSize>
        <Width>8.5in</Width>
        <Height>11in</Height>
    </PageSize>
    <Orientation>Portrait</Orientation>
</PageLayout>
"""

file_path = './tmp/page_layout.mif'

with open(file_path, 'w') as f:
    f.write(mif_content)

print(f"Generated MIF file with page layout features: {file_path}")
import os

# Create a folder to store the generated MIF files
os.makedirs('./tmp', exist_ok=True)

# Generate example MIF files with page layout features
mif_file_1 = """
<PageLayout>
    <Margins>
        <Top>1 inch</Top>
        <Bottom>1 inch</Bottom>
        <Left>1 inch</Left>
        <Right>1 inch</Right>
    </Margins>
    <Header>
        <Text>This is the header</Text>
    </Header>
    <Footer>
        <Text>This is the footer</Text>
    </Footer>
    <Orientation>Portrait</Orientation>
</PageLayout>
"""

mif_file_2 = """
<PageLayout>
    <Margins>
        <Top>0.5 inch</Top>
        <Bottom>0.5 inch</Bottom>
        <Left>0.5 inch</Left>
        <Right>0.5 inch</Right>
    </Margins>
    <Header>
        <Text>Header Section</Text>
    </Header>
    <Footer>
        <Text>Footer Section</Text>
    </Footer>
    <Orientation>Landscape</Orientation>
</PageLayout>
"""

# Save the generated MIF files into the tmp folder
with open('./tmp/page_layout_1.mif', 'w') as file:
    file.write(mif_file_1)

with open('./tmp/page_layout_2.mif', 'w') as file:
    file.write(mif_file_2)
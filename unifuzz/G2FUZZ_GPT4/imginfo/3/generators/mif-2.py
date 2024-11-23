import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the MIF file with formatting information
mif_content = """<MIFFile 9.00> # MIF version
<Units Uin> # Unit in inches
<Page
    <PageType Start>
    <PageSize 8.5" 11"> # Letter size
    <PageOrientation Portrait>
    <TextRect
        <ID 1>
        <TR_Page 1>
        <TR_FRect 1.0" 1.0" 6.5" 9.0"> # Text rectangle size
        <TR_Flow A>
    >
>
<Para
    <PgfTag `Heading1`>
    <PgfUseNextTag No>
    <PgfNumberingStyle NoNumber>
    <PgfSpBefore 12 pt>
    <PgfLineSpacing Fixed 14 pt>
    <Font
        <FTag `Arial`>
        <FSize 24.0>
        <FBold Yes>
    >
    <String `Formatted MIF Heading`>
>
<Para
    <PgfTag `Body`>
    <PgfUseNextTag No>
    <PgfNumberingStyle NoNumber>
    <PgfSpBefore 6 pt>
    <PgfLineSpacing Fixed 12 pt>
    <Font
        <FTag `Times New Roman`>
        <FSize 12.0>
        <FItalic Yes>
    >
    <String `This is an italicized text in the body paragraph. Formatting includes font styles, sizes, and paragraph styles.`>
>
"""

# Save the MIF content to a file
file_path = './tmp/example.mif'
with open(file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f"MIF file '{file_path}' has been generated successfully.")
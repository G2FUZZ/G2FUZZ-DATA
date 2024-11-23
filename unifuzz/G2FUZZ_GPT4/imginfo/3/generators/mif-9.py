import os

# Define the directory for saving the MIF files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# MIF content with bookmarks and table of contents
mif_content = """<MIFFile 9.00> # MIF file format version
<Book
    <TOC >
    <TocTitle `Table of Contents'>
    <Para
        <PgfTag `TOCHeading1'>
        <PgfNumTabs  0 >
        <PgfPlacement  :Anywhere >
        <PgfAlignment  :Left >
        <PgfFIndent  0.0" >
        <PgfLIndent  0.0" >
        <PgfRIndent  0.0" >
        <PgfSpBefore  0.0" >
        <PgfSpAfter  0.0" >
        <PgfWithPrev  No >
        <PgfWithNext  No >
        <PgfBlockSize  1 >
        <PgfFont
            <FTag `'>
            <FSize  24.0 pt >
            <FBold  Yes >
        > # End of PgfFont
        <String `Table of Contents'>
    > # End of Para
    <TOCEntry
        <Para
            <PgfTag `TOC1'>
            <PgfNumTabs  1 >
            <TabStop  7.5" Right >
            <String `Chapter 1: Introduction'>
            <Char Tab >
            <String `1'>
        > # End of Para
    > # End of TOCEntry
    <TOCEntry
        <Para
            <PgfTag `TOC1'>
            <PgfNumTabs  1 >
            <TabStop  7.5" Right >
            <String `Chapter 2: Getting Started'>
            <Char Tab >
            <String `5'>
        > # End of Para
    > # End of TOCEntry
    > # End of TOC
    <Bookmark
        <BkmkName `Chapter 1: Introduction'>
        <BkmkDest
            <Para
                <PgfTag `Heading1'>
                <String `Chapter 1: Introduction'>
            > # End of Para
        > # End of BkmkDest
    > # End of Bookmark
    <Bookmark
        <BkmkName `Chapter 2: Getting Started'>
        <BkmkDest
            <Para
                <PgfTag `Heading1'>
                <String `Chapter 2: Getting Started'>
            > # End of Para
        > # End of BkmkDest
    > # End of Bookmark
> # End of Book
"""

# Save the MIF content to a file
mif_file_path = os.path.join(output_dir, 'sample.mif')
with open(mif_file_path, 'w') as file:
    file.write(mif_content)

print(f'MIF file saved at {mif_file_path}')
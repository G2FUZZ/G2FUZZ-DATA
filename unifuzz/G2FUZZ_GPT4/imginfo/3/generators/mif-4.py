import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content for the MIF file, focusing on the table features description
mif_content = """<MIFFile 9.00> # Generated by Python
# FrameMaker MIF table example for representing complex table structures
<Frame
    <Pen 15>
    <Fill 7>
    <PenWidth  1.0 pt>
    <ObColor `Black'>
    <DashedPattern
        <DashedStyle Solid>
        <NumSegments  2>
        <DashSegment  7.0 pt>
        <DashSegment  3.0 pt>
    >
    <ShapeRect
        <BRect  1.0 in 1.0 in 6.0 in 4.0 in>
        <ShapeRectID 1>
    >
    <GroupID 1>
>
<Table
    <Tbls 1>
    <TblID 1>
    <TblFormat
        <TblTag `ExampleTable'>
        <TblTitle `Table: Complex Structures'>
        <TblPlacement Page>
        <TblStraddle No>
        <TblAlignment Center>
        <TblWidth 5.0 in>
        <TblNumColumns 3>
        <TblColumnWidths
            <ColumnWidth  1.667 in>
            <ColumnWidth  1.667 in>
            <ColumnWidth  1.667 in>
        >
        <TblBorder Yes>
        <TblBorderColor Black>
        <TblBorderWidth 0.5 pt>
        <TblCellMargins 0.2 in>
    >
    <TblH
        <THeader
            <TRow
                <TCell
                    <CellContent `Feature'>
                >
                <TCell
                    <CellContent `Description'>
                >
                <TCell
                    <CellContent `Notes'>
                >
            >
        >
    >
    <TblBody
        <TBody
            <TRow
                <TCell
                    <CellContent `Tables'>
                >
                <TCell
                    <CellContent `Support complex table structures, including formats, cell content, and styling'>
                >
                <TCell
                    <CellContent `Allows representation of tabulated data within the document'>
                >
            >
        >
    >
>
#End of MIF example
"""

# Save the MIF content to a file
with open('./tmp/table_feature.mif', 'w') as mif_file:
    mif_file.write(mif_content)
import os

# Create a directory to store the MIF files
os.makedirs('./tmp/', exist_ok=True)

# Generate MIF file with the given feature
mif_content = """MIF Version 3.00
Document
FontCatalog
    DefineFont Times-Roman
        Ascent 0.84375
        Descent 0.15625
        FamilyName "Times"
        FullName "Times-Roman"
        CharSet "ExtendedRoman"
        Weight "Roman"
        Italic "No"
        Underline "No"
        MonoSpaced "No"
        Proportional "Yes"
        Scalable "Yes"
        SmallCap "No"
        PointSize 12
    EndDef
EndFontCatalog
BodyPage
    Page
        Column
            ColumnWidth 504
            ColumnGutter 36
            Margins 72
        EndColumn
    EndPage
EndBodyPage
DocumentSetup
    PageWidth 648
    PageHeight 864
    TopMargin 72
    BottomMargin 72
    LeftMargin 72
    RightMargin 72
    ColumnCount 1
    ColumnGutter 36
    ColumnWidth 504
    Orientation Portrait
EndDocumentSetup
""".encode()

with open('./tmp/document.mif', 'wb') as f:
    f.write(mif_content)
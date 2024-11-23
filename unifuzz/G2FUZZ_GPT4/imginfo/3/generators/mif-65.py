import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the MIF file with various elements
mif_content = """
# MIF example with multiple elements
<MIFFile 9.00> # MIF version
<Units Ucm>    # Unit of measurement

# Define Text Flows
<TextFlow <ID 1> <TFTag `Body'>
    <Para <PgfTag `Heading1'>
        <String `Welcome to Our Guide'>
    >
    <Para <PgfTag `BodyText'>
        <String `For more detailed information, refer to our '>
        <Hypertext
            <AType `GoToURL'>
            <URL `http://www.example.com'>
            <NewWin No> >
        <String `website.'>
    >
    <Para <PgfTag `BodyText'>
        <String `This guide provides an overview of our services.'>
    >
>

<TextFlow <ID 2> <TFTag `Sidebar'>
    <Para <PgfTag `SidebarText'>
        <String `Sidebar Information: For additional resources, visit our website.'>
    >
>

# Define Pages with multiple elements
<Page <PN 1>
    <Frame <ID 1> <Pen 15> <Fill 7> <Shape Rect> <Angle 0> <DashedPattern <DashedStyle Solid>> <PenWidth 0.5> <BRect 2.0 cm 2.0 cm 6.0 cm 4.0 cm> <FrameType Below>
        <TextRect <ID 101> <TRNumColumns 1> <TRColumnGap 3.0> <TRColumnBalance No>
            <TFTag `Body'>
            <TRNextColumn No> <TRNextChain No> <TRColumnMinDepth 0> <TRColumnMaxDepth 0>
        >
    >
    <Frame <ID 2> <Pen 15> <Fill 7> <Shape Rect> <Angle 0> <DashedPattern <DashedStyle Solid>> <PenWidth 0.5> <BRect 8.5 cm 2.0 cm 12.5 cm 4.0 cm> <FrameType Below>
        <TextRect <ID 102> <TRNumColumns 1> <TRColumnGap 3.0> <TRColumnBalance No>
            <TFTag `Sidebar'>
            <TRNextColumn No> <TRNextChain No> <TRColumnMinDepth 0> <TRColumnMaxDepth 0>
        >
    >
    <Frame <ID 3> <Pen 15> <Fill 15> <Shape Rect> <Angle 0> <DashedPattern <DashedStyle Solid>> <PenWidth 0.5> <BRect 2.0 cm 6.5 cm 12.5 cm 9.5 cm> <FrameType Below>
        <Image <ID 201> <IGroupID 1> <Angle 0> <Flip No> <BitmapType Monochrome> <BRect 2.0 cm 6.5 cm 12.5 cm 9.5 cm>
            <FileName `./images/sample.jpg'> <BitMapDpi 72> <Color 7>
        >
    >
>

<Page <PN 2>
    # Additional page setup
    <Para <PgfTag `BodyText'>
        <String `This is the second page with more information and another image.'>
    >
    # Potential for more complex structures here
>

# End of the MIF file
"""

# Save the content to a .mif file in the ./tmp/ directory
file_path = './tmp/complex_example.mif'
with open(file_path, 'w') as file:
    file.write(mif_content.strip())

print(f'Complex MIF file created at: {file_path}')
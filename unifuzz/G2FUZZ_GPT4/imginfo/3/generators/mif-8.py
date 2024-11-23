import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path to the new MIF file
mif_file_path = './tmp/equations.mif'

# MIF content with a simplistic representation of an equation
mif_content = '''
# MIFFile 9.0

<Frame
    <ID 1>
    <PgfTag `Equation`>
    <GroupID 1>
    <Unique 1001>
    <Pen 15>
    <Fill 7>
    <PenWidth  0.5>
    <ObTir 0>
    <DashedPattern>
        <DashedStyle Solid>
    </DashedPattern>
    <Overprint No>
    <RunaroundType None>
    <RunaroundGap 0.0>
    <Angle 0.0>
    <Separation 0>
    <Spread None>
    <BRect 1.0 inch 1.0 inch 6.0 inch 4.0 inch>
    <Group
        <Math
            <MathFullForm `y = mx + b`>
            <MathSize 100>
            <MathFont `Times New Roman`>
        >
    >
>
'''

# Write the MIF content to the file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content.strip())

print(f'MIF file created at {mif_file_path}')
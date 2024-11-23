def create_mif_with_table():
    # MIF content to represent a table with formatting
    mif_content = """
<MIFFile 9.00> # MIF file version
<Units Ucm> # Units in centimeters

# Define a simple table
<Table
 <Tbls 1> # Start Table definition
 <TblID 1>
 <TblFormat
  <TblTag `TableWithFormatting`>
  <TblTitleContent
   <Para
    <PgfTag `TableTitle`>
    <ParaLine
     <String `Complex Table Example`>>>>
  <TblH # Table Header
   <Row
    <Cell <CellContent
     <Para
      <PgfTag `Heading1`>
      <ParaLine
       <String `Column 1`>>>>>
    <Cell <CellContent
     <Para
      <PgfTag `Heading2`>
      <ParaLine
       <String `Column 2`>>>>>>
  <TblBody # Table Body
   <Row
    <Cell <CellContent
     <Para
      <PgfTag `Body`>
      <ParaLine
       <String `Data 1`>>>>>
    <Cell <CellContent
     <Para
      <PgfTag `Body`>
      <ParaLine
       <String `Data 2`>>>>>>
   <Row
    <Cell <CellContent
     <Para
      <PgfTag `Body`>
      <ParaLine
       <String `Data 3`>>>>>
    <Cell <CellContent
     <Para
      <PgfTag `Body`>
      <ParaLine
       <String `Data 4`>>>>>>
  <TblF # Table Footer
   <Row
    <Cell <CellContent
     <Para
      <PgfTag `Footer`>
      <ParaLine
       <String `End of Table`>>>>>>
 >
"""

    # Specify the file path
    file_path = './tmp/table_example.mif'
    
    # Ensure the tmp directory exists
    import os
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Create and write the MIF content to a file
    with open(file_path, 'w') as file:
        file.write(mif_content.strip())

# Call the function to create the .mif file
create_mif_with_table()
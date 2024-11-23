import os

# Define the content of the MIF file
mif_content = """<MIFFile 7.00>
<Header
  MIFVersion = 7.00
  Creator = "Adobe FrameMaker"
  Product = "Adobe FrameMaker">
<Para
  <PgfCatalog
    <Pgf
      <PgfTag `ParagraphText'>
      <PgfLanguage `English'>
      <PgfFont "Times New Roman">
      <PgfSize 12
      <PgfLeading 14
      <PgfAlignment `Left'>
      <PgfHyphenate 1
      <PgfLetterSpace 0
    >
  >
>
<Para
  <PgfCatalog
    <Pgf
      <PgfTag `ParagraphText'>
      <PgfLanguage `English'>
      <PgfFont "Times New Roman">
      <PgfSize 12
      <PgfLeading 14
      <PgfAlignment `Left'>
      <PgfHyphenate 1
      <PgfLetterSpace 0
    >
  >
>
<Para
  <PgfCatalog
    <Pgf
      <PgfTag `ParagraphText'>
      <PgfLanguage `English'>
      <PgfFont "Times New Roman">
      <PgfSize 12
      <PgfLeading 14
      <PgfAlignment `Left'>
      <PgfHyphenate 1
      <PgfLetterSpace 0
    >
  >
>
<Para
  <PgfCatalog
    <Pgf
      <PgfTag `ParagraphText'>
      <PgfLanguage `English'>
      <PgfFont "Times New Roman">
      <PgfSize 12
      <PgfLeading 14
      <PgfAlignment `Left'>
      <PgfHyphenate 1
      <PgfLetterSpace 0
    >
  >
>
<Para
  <PgfCatalog
    <Pgf
      <PgfTag `ParagraphText'>
      <PgfLanguage `English'>
      <PgfFont "Times New Roman">
      <PgfSize 12
      <PgfLeading 14
      <PgfAlignment `Left'>
      <PgfHyphenate 1
      <PgfLetterSpace 0
    >
  >
>
<Para
  <PgfCatalog
    <Pgf
      <PgfTag `ParagraphText'>
      <PgfLanguage `English'>
      <PgfFont "Times New Roman">
      <PgfSize 12
      <PgfLeading 14
      <PgfAlignment `Left'>
      <PgfHyphenate 1
      <PgfLetterSpace 0
    >
  >
>
<Para
  <PgfCatalog
    <Pgf
      <PgfTag `ParagraphText'>
      <PgfLanguage `English'>
      <PgfFont "Times New Roman">
      <PgfSize 12
      <PgfLeading 14
      <PgfAlignment `Left'>
      <PgfHyphenate 1
      <PgfLetterSpace 0
    >
  >
>
<Para
  <PgfCatalog
    <Pgf
      <PgfTag `ParagraphText'>
      <PgfLanguage `English'>
      <PgfFont "Times New Roman">
      <PgfSize 12
      <PgfLeading 14
      <PgfAlignment `Left'>
      <PgfHyphenate 1
      <PgfLetterSpace 0
    >
  >
>
Compatibility: Designed for use with Adobe FrameMaker, but can be imported into other DTP tools.
"""

# Create the tmp directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Save the content to a .mif file in the tmp directory
with open('./tmp/generated_file.mif', 'w') as f:
    f.write(mif_content)

print("MIF file generated successfully.")
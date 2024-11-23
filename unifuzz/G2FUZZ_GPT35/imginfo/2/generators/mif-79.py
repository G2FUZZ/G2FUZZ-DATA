import os

# Define the content of the extended mif file
extended_mif_content = """
<MIFFile 7.0>
<CharacterMapping <<
<Name (DefaultParagraphFont <Minion Pro><R=0,G=0,B=0>) <MacPSRoman> >>
>>
<DefaultFont <Minion Pro>>
<VariableFont <MyVariableFont>>
<DefaultColor <BlackColor>>
<DefaultSwatch <NoColorSwatch>>
<DefaultTable <NoTable>>
<DefaultTextFrame <NoTextFrame>>
<DefaultPage <NoPage>>
<DefaultMasterPage <MyMasterPage>>
<DefaultReferencePage <MyReferencePage>>
<DefaultLayer <MyLayer>>
<DefaultConditionalTextTag <MyConditionalTextTag>>
<DefaultCondition <MyCondition>>
<DefaultTableColumn <MyTableColumn>>
<DefaultTableRow <MyTableRow>>
<DefaultInsertionPoint <MyInsertionPoint>>
<DefaultTextLine <MyTextLine>>
<DefaultTextColumn <MyTextColumn>>
<DefaultText <MyText>>
<DefaultPosition <MyPosition>>
<DefaultAnchor <MyAnchor>>
<DefaultMarker <MyMarker>>
<DefaultObject <MyObject>>
<DefaultFrame <MyFrame>>
<DefaultGraphic <MyGraphic>>
<DefaultTable <MyTable>>
<DefaultCell <MyCell>>
<DefaultRow <MyRow>>
<DefaultColumn <MyColumn>>
<DefaultImage <MyImage>>
<DefaultImport <MyImport>>
<DefaultLink <MyLink>>
<DefaultCondition <MyCondition>>
<DefaultXMLElement <MyXMLElement>>
<DefaultXMLAttribute <MyXMLAttribute>>
<DefaultTextVariableInstance <MyTextVariableInstance>>
<DefaultCrossReferenceFormat <MyCrossReferenceFormat>>
<DefaultIndexFormat <MyIndexFormat>>
<DefaultParagraphStyle <MyParagraphStyle>>
<DefaultCharacterStyle <MyCharacterStyle>>
<DefaultTableStyle <MyTableStyle>>
<DefaultCellStyle <MyCellStyle>>
<DefaultObjectStyle <MyObjectStyle>>
<DefaultRootStyle <MyRootStyle>>
<DefaultConditionalTextTag <MyConditionalTextTag>>
<DefaultVariable <MyVariable>>
<DefaultXMLComment <MyXMLComment>>
<DefaultXMLElement <MyXMLElement>>
<DefaultXMLElementType <MyXMLElementType>>
<DefaultSVVariable <MySVVariable>>
<DefaultSVVariableInstance <MySVVariableInstance>>
<DefaultChange <MyChange>>
<DefaultChangeList <MyChangeList>>
<DefaultChangePage <MyChangePage>>
<DefaultChangeColumn <MyChangeColumn>>
<DefaultChangeRow <MyChangeRow>>
<DefaultChangeCell <MyChangeCell>>
<DefaultChangeLine <MyChangeLine>>
<DefaultChangeText <MyChangeText>>
<DefaultChangeFrame <MyChangeFrame>>
<DefaultChangeGraphic <MyChangeGraphic>>
<DefaultChangeMarker <MyChangeMarker>>
<DefaultChangeImage <MyChangeImage>>
<DefaultChangeCondition <MyChangeCondition>>
<DefaultChangeTable <MyChangeTable>>
<DefaultChangeObject <MyChangeObject>>
<DefaultChangeXMLElement <MyChangeXMLElement>>
<DefaultChangeXMLElementType <MyChangeXMLElementType>>
<DefaultChangeTextVariableInstance <MyChangeTextVariableInstance>>
<DefaultChangeCrossReferenceFormat <MyChangeCrossReferenceFormat>>
<DefaultChangeIndexFormat <MyChangeIndexFormat>>
<DefaultChangeParagraphStyle <MyChangeParagraphStyle>>
<DefaultChangeCharacterStyle <MyChangeCharacterStyle>>
<DefaultChangeTableStyle <MyChangeTableStyle>>
<DefaultChangeCellStyle <MyChangeCellStyle>>
<DefaultChangeObjectStyle <MyChangeObjectStyle>>
<DefaultChangeRootStyle <MyChangeRootStyle>>
<DefaultChangeConditionalTextTag <MyChangeConditionalTextTag>>
<DefaultChangeVariable <MyChangeVariable>>
<DefaultChangeXMLComment <MyChangeXMLComment>>
<DefaultChangeXMLElement <MyChangeXMLElement>>
<DefaultChangeSVVariable <MyChangeSVVariable>>
<DefaultChangeSVVariableInstance <MyChangeSVVariableInstance>>
<DefaultChangeCondition <MyChangeCondition>>
>>
"""

# Create the extended tmp directory if it doesn't exist
os.makedirs('./tmp/extended/', exist_ok=True)

# Save the extended mif file with the specified content
extended_file_path = './tmp/extended/extended_platform_independent.mif'
with open(extended_file_path, 'w') as f:
    f.write(extended_mif_content)

print(f'Extended MIF file generated: {extended_file_path}')
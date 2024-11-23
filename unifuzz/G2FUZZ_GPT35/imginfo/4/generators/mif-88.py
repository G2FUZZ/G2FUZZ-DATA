import os

# Create a directory if it doesn't exist
os.makedirs("./tmp/", exist_ok=True)

# Generate complex mif file with nested conditional text blocks and variable placeholders
mif_content = """
<ConditionalText>
<VariableDefs>
<VariableDef Name="var_1" Type="String" DefaultValue="Hello"/>
<VariableDef Name="var_2" Type="String" DefaultValue="World"/>
</VariableDefs>
<ConditionSet Name="condition_set">
<Condition Name="condition_1" Expression="var_1 == 'Hello'"/>
<Condition Name="condition_2" Expression="var_2 == 'World'"/>
</ConditionSet>
<ConditionalTextBlock>
<ConditionRef Condition="condition_1"/>
<ConditionalTextBlock>
<ConditionRef Condition="condition_2"/>
{ var_1 }, { var_2 }! This is a nested conditional text block.
</ConditionalTextBlock>
</ConditionalTextBlock>
<ConditionalTextBlock>
<Default/>
Default text when no conditions are met.
</ConditionalTextBlock>
</ConditionalText>
"""

# Save mif file into tmp directory
with open("./tmp/extended_conditional_text.mif", "w") as f:
    f.write(mif_content)

print("Generated extended mif file with complex features successfully.")
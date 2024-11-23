import os

# Create a directory if it doesn't exist
os.makedirs("./tmp/", exist_ok=True)

# Generate mif file with conditional text
mif_content = """
<ConditionalText>
<ConditionSet Name="condition_set">
<Condition Name="condition_1" Expression="1 == 1"/>
<Condition Name="condition_2" Expression="2 == 1"/>
</ConditionSet>
<ConditionalTextBlock>
<ConditionRef Condition="condition_1"/>
This is displayed when condition_1 is true.
</ConditionalTextBlock>
<ConditionalTextBlock>
<ConditionRef Condition="condition_2"/>
This is displayed when condition_2 is true.
</ConditionalTextBlock>
<ConditionalTextBlock>
<Default/>
This is displayed when no conditions are met.
</ConditionalTextBlock>
</ConditionalText>
"""

# Save mif file into tmp directory
with open("./tmp/conditional_text.mif", "w") as f:
    f.write(mif_content)

print("Generated mif file with conditional text successfully.")
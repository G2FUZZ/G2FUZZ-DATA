import os

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

# Function to create a MIF file with conditional text
def create_mif_with_conditional_text(filename, condition):
    content = f"""<MIFFile 9.00>
# The condition for showing text
<Condition
    <CondTag `{condition}`>
    <CondState Show>
>
# The conditional text
<Conditional
    <CondText
        <Para
            <PgfTag `Body`>
            <CondTag `{condition}`>
            <String `This is conditional text visible only if the condition "{condition}" is met.`>
        >
    >
>
# Closing the condition tag
<ConditionEnd>
</MIFFile>
"""
    with open(os.path.join(output_dir, filename), 'w') as mif_file:
        mif_file.write(content)

# Example conditions
conditions = ['Condition1', 'Condition2']

# Generate MIF files for each condition
for condition in conditions:
    filename = f"example_with_{condition}.mif"
    create_mif_with_conditional_text(filename, condition)

print("MIF files with conditional text have been generated.")
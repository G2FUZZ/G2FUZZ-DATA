import json
import os

# Generate pixdata file with Transparency feature
transparency_data = {
    "Transparency": "Supports transparency or alpha blending"
}

output_dir = "./tmp/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file = os.path.join(output_dir, "pixdata_transparency.json")
with open(output_file, "w") as file:
    json.dump(transparency_data, file, indent=4)

print(f"Generated pixdata file with Transparency feature saved at {output_file}")
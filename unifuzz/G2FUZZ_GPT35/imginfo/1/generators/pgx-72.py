import os

sections = {
    "Introduction": "This is the introduction section.",
    "Features": "This section contains the features of the file format.",
    "Usage": "Here's how you can use the file format.",
    "Examples": "Some examples to showcase the file format."
}

file_content = ""
for section_title, section_content in sections.items():
    file_content += f"{section_title}:\n{section_content}\n\n"

file_path = "./tmp/complex_feature_file.pgx"

os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, "w") as file:
    file.write(file_content)

print(f"Complex File saved at {file_path}")
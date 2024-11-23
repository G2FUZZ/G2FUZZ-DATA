import os

features = "8. Compatibility: 'pgx' files may be compatible with specific software or platforms for editing and viewing."

file_content = f"Features:\n{features}"

file_path = "./tmp/feature_file.pgx"

os.makedirs(os.path.dirname(file_path), exist_ok=True)

with open(file_path, "w") as file:
    file.write(file_content)

print(f"File saved at {file_path}")
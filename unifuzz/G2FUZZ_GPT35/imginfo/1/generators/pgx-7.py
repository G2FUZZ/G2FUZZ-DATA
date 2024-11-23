import os

# Define the content for the pgx file
content = "Layers: Some 'pgx' files may support multiple layers, allowing for complex image compositions."

# Create the tmp directory if it does not exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the content to a pgx file
with open('./tmp/example.pgx', 'w') as file:
    file.write(content)

print("pgx file created successfully at ./tmp/example.pgx")
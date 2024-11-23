import gzip

# Create a sample data to be saved in the pgx file
data = "Sample data to be saved in a pgx file."

# Save the data in a pgx file without compression
with open('./tmp/sample.pgx', 'w') as file:
    file.write(data)

# Save the data in a compressed pgx file
with gzip.open('./tmp/sample_compressed.pgx', 'wt') as file:
    file.write(data)
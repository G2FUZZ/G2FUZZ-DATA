def calculate_sum(a, b):
    return a + b

result = calculate_sum(3, 5)
print(result)

# Save the result into a file in the ./tmp/ directory
with open('./tmp/result.txt', 'w') as file:
    file.write(str(result))
def greet(name):
    message = "Hello, " + name + "!"
    # Save the greeting into a file in the ./tmp/ directory
    with open('./tmp/greeting.txt', 'w') as file:
        file.write(message)

greet("Alice")
import os

# Ensure the ./tmp/ directory exists
try:
    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
        print("Directory './tmp/' was created successfully.")
    else:
        print("Directory './tmp/' already exists.")
except Exception as e:
    print(f"An error occurred while creating './tmp/': {e}")
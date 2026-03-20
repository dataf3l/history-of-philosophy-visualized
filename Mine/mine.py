import json

# Assuming your file is named 'data.json'
file_path = 'data.json'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
        # Accessing the 'people' list and printing each name
        print("List of Philosophers:")
        print("-" * 20)
        for person in data.get('people', []):
            print(person.get('name'))

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON. Check the file format.")

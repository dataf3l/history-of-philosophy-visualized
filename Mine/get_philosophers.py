import json

# Configuration
input_file = 'data.json'
output_file = 'philosopher_names.txt'

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract names and write them immediately
    with open(output_file, 'w', encoding='utf-8') as out:
        for person in data.get('people', []):
            name = person.get('name', 'Unknown')
            out.write(name + '\n')

    print(f"Success: Names written to {output_file}")

except Exception as e:
    print(f"File Error: {e}")
import json

# Path to your source data
source_file = 'data.json'

try:
    with open(source_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Create a lookup dictionary: {id: name}
    # This makes searching for a name by ID much faster
    philosopher_lookup = {p['id']: p['name'] for p in data.get('people', [])}

    # 2. Correlate and write to claims2.txt
    records = data.get('records', [])
    
    with open('claims2.txt', 'w', encoding='utf-8') as output_file:
        for entry in records:
            # Get the person ID from the record
            person_id = entry.get('person')
            # Look up the name using the ID; default to 'Unknown' if not found
            name = philosopher_lookup.get(person_id, "Unknown Philosopher")
            # Get the claim text
            claim = entry.get('line', "No claim text found")
            
            # Write in the format: phil_name|claim
            output_file.write(f"{name}|{claim}\n")

    print("Done! 'claims2.txt' has been generated with mapped names.")

except FileNotFoundError:
    print(f"Error: {source_file} not found.")
except Exception as e:
    print(f"An error occurred: {e}")

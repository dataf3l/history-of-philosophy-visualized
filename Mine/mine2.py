import json

# Path to your source data
source_file = 'data.json'

try:
    with open(source_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    records = data.get('records', [])

    # 1. Create references.txt
    with open('references.txt', 'w', encoding='utf-8') as ref_file:
        for entry in records:
            ref = entry.get('reference')
            if ref:
                ref_file.write(f"{ref}\n")
    
    # 2. Create claims.txt (mapped to the 'line' field in your JSON)
    with open('claims.txt', 'w', encoding='utf-8') as claims_file:
        for entry in records:
            claim = entry.get('line')
            if claim:
                claims_file.write(f"{claim}\n")

    print("Success! 'references.txt' and 'claims.txt' have been created.")

except FileNotFoundError:
    print(f"Error: {source_file} not found.")
except json.JSONDecodeError:
    print("Error: The JSON file is malformed.")

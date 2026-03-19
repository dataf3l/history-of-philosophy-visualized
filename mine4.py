import json
from collections import Counter

# Path to your source data
source_file = 'data.json'

try:
    with open(source_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Extract all references from the records list
    records = data.get('records', [])
    all_refs = [entry.get('reference') for entry in records if entry.get('reference')]

    # 2. Count the frequency of each unique reference
    ref_counts = Counter(all_refs)

    # 3. Sort by count (descending) then by name (alphabetical)
    # .most_common() returns a list of (element, count) sorted by count
    sorted_refs = ref_counts.most_common()

    # 4. Write to references.txt
    with open('references.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(f"{'REFERENCE':<70} | {'COUNT'}\n")
        output_file.write("-" * 80 + "\n")
        
        for ref, count in sorted_refs:
            output_file.write(f"{ref} | {count}\n")

    print(f"Done! Processed {len(all_refs)} total references into {len(ref_counts)} unique entries.")

except FileNotFoundError:
    print(f"Error: {source_file} not found.")
except Exception as e:
    print(f"An error occurred: {e}")

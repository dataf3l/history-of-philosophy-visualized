import sys
import stanza
import json
import time
from collections import defaultdict

def build_nested_dict(node_id, tree_map, words_map):
    """Recursively builds a nested dictionary representing the tree."""
    word_info = words_map[node_id]
    node = {
        "text": word_info['text'],
        "pos": word_info['pos'],
        "dep": word_info['dep'],
        "children": []
    }
    for child_id in tree_map[node_id]:
        node["children"].append(build_nested_dict(child_id, tree_map, words_map))
    return node

def run_analysis(input_file, output_file):
    # 1. Track Model Loading Time
    print(f"--- Initializing Stanford Stanza ---")
    start_load = time.time()
    try:
        nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse', verbose=False)
    except Exception:
        stanza.download('en')
        nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse', verbose=False)
    end_load = time.time()
    print(f"Model Load Time: {end_load - start_load:.2f} seconds")

    # 2. Read Input File
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            full_text = f.read()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return

    # 3. Process Sentences and Track Generation Time
    print(f"Processing text and generating trees...")
    start_gen = time.time()
    
    doc = nlp(full_text)
    all_sentences_trees = []

    for stanza_sent in doc.sentences:
        tree_map = defaultdict(list)
        words_map = {}
        root_id = -1

        for word in stanza_sent.words:
            words_map[word.id] = {
                'text': word.text,
                'pos': word.xpos,
                'dep': word.deprel
            }
            if word.head == 0:
                root_id = word.id
            else:
                tree_map[word.head].append(word.id)

        if root_id != -1:
            sentence_tree = build_nested_dict(root_id, tree_map, words_map)
            all_sentences_trees.append(sentence_tree)

    end_gen = time.time()
    
    # 4. Save to JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_sentences_trees, f, indent=4)

    print(f"Tree Generation Time: {end_gen - start_gen:.2f} seconds")
    print(f"Success: {len(all_sentences_trees)} trees saved to {output_file}")

if __name__ == "__main__":
    # Check for custom input file in argv, otherwise default to input.txt
    input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    output_path = "example.json"
    
    run_analysis(input_path, output_path)

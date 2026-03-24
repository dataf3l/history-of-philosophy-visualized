import sys
import stanza
import json
from collections import defaultdict

# Initialize Stanza
try:
    nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse', verbose=False)
except Exception:
    stanza.download('en')
    nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse', verbose=False)

def build_nested_dict(node_id, tree_map, words_map):
    """
    Recursively builds a nested dictionary representing the tree.
    """
    word_info = words_map[node_id]
    
    # Create the node for the current word
    node = {
        "text": word_info['text'],
        "pos": word_info['pos'],
        "dep": word_info['dep'],
        "children": []
    }
    
    # Recursively add all children
    for child_id in tree_map[node_id]:
        node["children"].append(build_nested_dict(child_id, tree_map, words_map))
        
    return node

def run_analysis(sentence):
    doc = nlp(sentence)
    
    all_sentences_trees = []

    for stanza_sent in doc.sentences:
        tree_map = defaultdict(list)
        words_map = {}
        root_id = -1

        # 1. Map words and their relationships
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

        # 2. Build the nested JSON structure
        if root_id != -1:
            sentence_tree = build_nested_dict(root_id, tree_map, words_map)
            all_sentences_trees.append(sentence_tree)

    # 3. Output the Nested JSON
    print(json.dumps(all_sentences_trees, indent=4))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_sentence = " ".join(sys.argv[1:])
        run_analysis(input_sentence)
    else:
        print("Usage: python script.py \"Your sentence here\"")

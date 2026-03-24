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

def print_ascii_tree(node_id, tree_map, words_map, prefix="", is_last=True):
    """Recursively prints the dependency tree using ASCII."""
    word_info = words_map[node_id]
    connector = "+-- " if is_last else "|-- "
    print(f"{prefix}{connector}{word_info['pos']}: {word_info['text']} ({word_info['dep']})")
    
    new_prefix = prefix + ("    " if is_last else "|   ")
    children = tree_map[node_id]
    for i, child_id in enumerate(children):
        print_ascii_tree(child_id, tree_map, words_map, new_prefix, i == len(children) - 1)

def run_analysis(sentence):
    doc = nlp(sentence)
    
    # 1. Print JSON Representation
    # .to_dict() converts the Stanza Document into a list of lists of dictionaries
    print("--- JSON REPRESENTATION ---")
    print(json.dumps(doc.to_dict(), indent=4))
    print("\n" + "="*50 + "\n")

    # 2. Print ASCII Tree
    print("--- ASCII HIERARCHY ---")
    for i, stanza_sent in enumerate(doc.sentences):
        print(f"Sentence {i+1}:")
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
            print_ascii_tree(root_id, tree_map, words_map)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_sentence = " ".join(sys.argv[1:])
        run_analysis(input_sentence)
    else:
        print("Usage: python script.py \"Your sentence here\"")

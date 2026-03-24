import sys
import stanza
from collections import defaultdict

# Setup the Stanford Stanza pipeline (English)
# 'depparse' is the key processor that creates the tree structure
try:
    nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse', verbose=False)
except Exception:
    # Fallback if models aren't downloaded yet
    stanza.download('en')
    nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse', verbose=False)

def print_ascii_tree(node_id, tree_map, words_map, prefix="", is_last=True):
    """
    Recursively prints the dependency tree using only ASCII characters.
    """
    word_info = words_map[node_id]
    
    # Use standard ASCII markers
    connector = "+-- " if is_last else "|-- "
    
    # Display: POS_TAG: Word (Grammatical Role)
    print(f"{prefix}{connector}{word_info['pos']}: {word_info['text']} ({word_info['dep']})")
    
    # Create the indentation prefix for the next level
    # If this is the last child, we don't draw a vertical line down
    new_prefix = prefix + ("    " if is_last else "|   ")
    
    children = tree_map[node_id]
    for i, child_id in enumerate(children):
        print_ascii_tree(child_id, tree_map, words_map, new_prefix, i == len(children) - 1)

def run_analysis(sentence):
    doc = nlp(sentence)

    for i, stanza_sent in enumerate(doc.sentences):
        print(f"\n[Sentence {i+1} Hierarchy]")
        print("ROOT") # The starting point
        
        tree_map = defaultdict(list)
        words_map = {}
        root_id = -1

        # 1. Map out the parent-child relationships
        for word in stanza_sent.words:
            words_map[word.id] = {
                'text': word.text,
                'pos': word.xpos,
                'dep': word.deprel
            }
            if word.head == 0:
                root_id = word.id
            else:
                # word.head is the ID of the 'governor' (parent)
                tree_map[word.head].append(word.id)

        # 2. Start the recursive print from the root word
        if root_id != -1:
            print_ascii_tree(root_id, tree_map, words_map)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_sentence = " ".join(sys.argv[1:])
        run_analysis(input_sentence)
    else:
        print("Usage: python script.py \"Your sentence here\"")

import sys
import stanza

# Standard symbols for Unix-tree style
# +-- (Branch)
# +-- (Last leaf)
#     (Vertical pipe)

def print_unix_tree(label, children, prefix=""):
    """
    Recursively prints a tree in the style of the Unix 'tree' command.
    """
    count = len(children)
    for i, (word, pos) in enumerate(children):
        is_last = (i == count - 1)
        connector = "+-- " if is_last else "+-- "
        
        # Print the POS tag and the word
        print(f"{prefix}{connector}{pos}: {word}")

def run_modern_pos_tree(sentence):
    # Initialize Stanford Stanza (Quiet mode)
    nlp = stanza.Pipeline(lang='en', processors='tokenize,pos', verbose=False)
    doc = nlp(sentence)

    for i, stanza_sent in enumerate(doc.sentences):
        print(f"\n[Sentence {i+1}]")
        print(".") # Root of the "directory"
        
        # Prepare the list of (word, tag)
        # Using xpos for traditional Penn Treebank tags (NN, VBZ, etc.)
        nodes = [(word.text, word.xpos) for word in stanza_sent.words]
        
        # Render in Unix style
        print_unix_tree("S", nodes)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_sentence = " ".join(sys.argv[1:])
        run_modern_pos_tree(input_sentence)
    else:
        print("Usage: python script.py Your sentence here")

import sys
import stanza
from nltk import Tree

def run_stanford_pos(sentence):
    # 1. Download/Initialize the Stanford English pipeline
    # 'upos' is the Universal POS processor
    print("Initializing Stanford/Stanza pipeline...")
    nlp = stanza.Pipeline(lang='en', processors='tokenize,pos', tokenize_no_ssplit=True)

    # 2. Process the text
    doc = nlp(sentence)

    # 3. Extract words and their POS tags
    # Stanza organizes things as: Document -> Sentence -> Word
    tagged_data = []
    for sent in doc.sentences:
        for word in sent.words:
            # xpos is the Penn Treebank style tag (NN, VBZ, etc.)
            # upos is the Universal tag (NOUN, VERB)
            tagged_data.append((word.text, word.xpos))

    # 4. Create and print the tree
    tree = Tree('S', tagged_data)
    print(f"\nStanford POS Analysis: \"{sentence}\"")
    print("-" * 40)
    tree.pretty_print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_sentence = " ".join(sys.argv[1:])
        run_stanford_pos(input_sentence)
    else:
        print("Usage: python script.py \"Your sentence here\"")

import sys
import nltk
from nltk import pos_tag, word_tokenize
from nltk.tree import Tree

# Download necessary NLTK data (only runs once if already present)
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

def print_pos_tree(sentence):
    # Tokenize and Tag
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)
    
    # Create and print the tree
    tree = Tree('S', tagged)
    print(f"\nProcessing: \"{sentence}\"")
    print("-" * 30)
    tree.pretty_print()

if __name__ == "__main__":
    # Check if an argument was passed (sys.argv[0] is the script name)
    if len(sys.argv) > 1:
        # Join all arguments after the script name into one string
        # This allows you to type: python script.py This is a test
        input_sentence = " ".join(sys.argv[1:])
        print_pos_tree(input_sentence)
    else:
        print("Error: Please provide a sentence as a command line argument.")
        print("Usage: python script_name.py \"Your sentence here\"")

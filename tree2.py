import sys
from allennlp.predictors.predictor import Predictor
import allennlp_models.structured_prediction  # Registers the tagging models
from nltk import Tree

def run_allen_pos(sentence):
    # 1. Load the pre-trained POS tagger model
    # Note: This will download the model weights (~several hundred MB) on first run
    model_url = "https://storage.googleapis.com/allennlp-public-models/structured-prediction-pos-tagging-2020.06.17.tar.gz"
    
    try:
        predictor = Predictor.from_path(model_url)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # 2. Run prediction
    prediction = predictor.predict(sentence=sentence)
    
    # AllenNLP returns a dictionary. We want 'words' and 'tags'.
    words = prediction['words']
    tags = prediction['tags']
    
    # 3. Create a Tree for printing
    # We zip the words and tags together as tuples for the NLTK Tree
    tagged_data = list(zip(words, tags))
    tree = Tree('S', tagged_data)
    
    # 4. Print results
    print(f"\nAllenNLP Analysis: \"{sentence}\"")
    print("-" * 40)
    tree.pretty_print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_sentence = " ".join(sys.argv[1:])
        run_allen_pos(input_sentence)
    else:
        print("Usage: python script.py \"Your sentence here\"")

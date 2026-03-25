# Philosophy Visualized - A Guide for Everyone

Welcome to **Philosophy Visualized**! This project is designed to bridge the gap between complex philosophical text and beautiful, generated pixel-art "forests." 

Whether you are a seasoned developer, a philosophy student, or simply someone who appreciates data art, this guide is written specifically for you. You don't need any prior programming experience to get this running on your own computer. We will walk you through every single step, from installing Python to generating your first massive visual forest.

---

## 🌟 Acknowledgements & Community Credit

Before we begin, we must thank the incredible open-source community. This project stands on the shoulders of giants. We are deeply grateful to the authors and contributors of the following libraries, without whom this tool would simply not exist:

- **[Stanford Stanza](https://stanfordnlp.github.io/stanza/)**: Developed by the Stanford NLP Group, Stanza provides incredibly accurate, state-of-the-art natural language processing. It is the core engine we use to understand the complex grammatical structures of philosophical writing.
- **[NLTK (Natural Language Toolkit)](https://www.nltk.org/)**: A foundational library for NLP in Python, which paved the way for computational linguistics.
- **[AllenNLP](https://guide.allennlp.org/)**: Developed by the Allen Institute for AI, providing robust deep learning models for text analysis.
- **[Pillow (PIL)](https://python-pillow.org/)**: The friendly Python Imaging Library fork, which we use to draw and render our beautiful pixel-art syntax trees.

To all the researchers, developers, and maintainers of these projects: **Thank You.**

---

## 🛠️ Step 1: Installing Python

To run these scripts, your computer needs to understand the Python programming language. 

1. **Download Python**: Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click the big yellow button that says **Download Python** (make sure it's version 3.8 or newer).
3. **CRITICAL STEP (Windows Users)**: When you open the installer, before you click "Install Now," you **must check the box at the bottom that says "Add Python to PATH"** or "Add python.exe to PATH". If you miss this, your computer won't know how to run Python commands!
4. Click "Install Now" and wait for it to finish.

---

## 📦 Step 2: Preparing the Project environment

Instead of installing our required libraries globally on your computer (which can cause messy conflicts later), we will use something called a **Virtual Environment** (`venv`). Think of it as an isolated, dedicated workspace just for this project.

1. **Open your Terminal / Command Prompt**:
   - **Windows**: Press the `Windows` key, type `cmd`, and hit Enter.
   - **Mac/Linux**: Open the `Terminal` application.

2. **Navigate to this project folder**:
   Use the `cd` (change directory) command to go to where you saved this project. For example:
   ```cmd
   cd path/to/philosophy-visualized
   ```

3. **Create the Virtual Environment**:
   Type the following command and hit Enter. (It might take a few seconds and won't show any output when it's done).
   ```cmd
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:
   You must do this every time you open a new terminal to work on this project.
   - **Windows**:
     ```cmd
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```cmd
     source venv/bin/activate
     ```
   *You'll know it worked if you see `(venv)` appear at the very beginning of your command line text.*

5. **Install the Dependencies**:
   Now, we download the community libraries mentioned in the acknowledgements.
   ```cmd
   pip install stanza nltk allennlp pillow
   ```
   *(Note: This might take a few minutes to download all the necessary files.)*

---

## 🚀 Step 3: Running the Pipeline

The core workflow relies on two main scripts: `tree8.py` (to read the text and build the tree structure) and `treeviz-a.py` (to draw the actual picture).

### 1. Parse the Text
This step reads documents (like Kant or Hegel) and uses Stanford Stanza to map out the grammar.
```cmd
python tree8.py
```
*Note: The first time you run this, it will download large AI models to your computer. Depending on the size of the book, parsing can take anywhere from 2 to 15 minutes.*

### 2. Draw the Forest (Unsorted)
Once the `.json` file is prepared, we can draw the pixel art!
```cmd
python treeviz-a.py example.json my-first-forest.png
```

### 3. Draw the Forest (Sorted by Tree Depth)
You can organize the forest so the most complex grammatical trees appear grouped together.
```cmd
python treeviz-a.py --sort-depth example.json my-sorted-forest.png
```

---

## 📊 Performance & Scale Notes

This tool is designed to handle immense scale. Based on real tests parsing dense philosophical texts, Stanford Stanza outputs highly detailed NLP data. Generating the PNGs produces massive, sprawling images representing thousands of tree structures:

- **Kant's Critique**: ~6,200 sentences (takes ~11.5 mins to parse). Generates a massive 79x79 grid image.
- **Hegel**: ~4,500 sentences (takes ~7 mins to parse). Generates a 68x68 grid image.
- **Tractatus**: ~2,900 sentences (takes ~3.5 mins to parse). Generates a 55x54 grid image.
- **Russell**: ~1,600 sentences (takes ~2.5 mins to parse). Generates a 41x41 grid image.

While the parsing step requires heavy computation, the rendering step processes these thousands of trees almost instantly. The resulting maps are extraordinarily large, with some images exceeding 40,000 pixels in width!

---

## 📂 Understanding the Scripts

If you're curious about taking a peek under the hood, here is a breakdown of what the files in this folder actually do. They show the history of how this project evolved:

### Parsing Scripts (Text to Data)
- `tree.py`: Demonstrates basic Part-of-Speech (POS) tagging using NLTK.
- `tree2.py`: Uses AllenNLP to generate POS tags.
- `tree3.py`: Upgrades to Stanford Stanza for basic POS tagging.
- `tree4.py`: Prints Stanza's POS analysis in a style similar to Unix directory trees.
- `tree5.py`: Advances to dependency parsing (finding how words relate to each other) and prints an ASCII diagram.
- `tree6.py`: Outputs both a JSON dictionary representation and an ASCII tree.
- `tree7.py`: Builds a nested JSON dictionary representing exact mathematical child-parent grammatical relationships.
- `tree8.py`: **The main production parser**. Reads a full book from `input.txt`, analyzes it, and saves it to a `.json` file, tracking performance times as it goes.

### Visualization Scripts (Data to Art)
- `treeviz.py`: Takes the JSON data and draws a basic pixel-forest PNG, representing nodes as simple 3x3 pixel blocks.
- `treeviz-a.py`: **The main visualizer**. An advanced version offering custom layouts (`--cols`, `--sort-depth`, `--node-size`, etc.) capable of handling and organizing full books into single massive PNG files.

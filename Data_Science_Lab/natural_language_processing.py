# Import necessary NLTK libraries and modules
import nltk
from nltk.tokenize import word_tokenize      # For tokenizing text into words
from nltk import pos_tag                     # For Part-of-Speech tagging
from nltk import RegexpParser                # For chunking using regular expressions
from nltk import ngrams
from nltk.probability import LidstoneProbDist

# Download required NLTK data files (quiet=True to hide logs)
nltk.download('punkt', quiet=True)                      # Tokenizer model
nltk.download('averaged_perceptron_tagger', quiet=True) # POS tagging model
nltk.download('maxent_ne_chunker', quiet=True)          # For named entity recognition
nltk.download('words', quiet=True)                      # Dictionary words for chunking

# Input text for tokenization and POS tagging
text = "Part of speech tagging is a natural language processing task."

# ----------------- Step 1: TOKENIZATION -----------------
tokens = word_tokenize(text)
print("=====Tokens=====\n\n", tokens)

# ----------------- Step 2: PART-OF-SPEECH (POS) TAGGING -----------------
pos_tags = pos_tag(tokens)
print("\n===== Part of Speech Tags=====\n")
for word, tag in pos_tags:
    print(f"{word} → {tag}")

# ----------------- Step 3: N-GRAM SMOOTHING -----------------

# Function to calculate n-gram probabilities using Lidstone smoothing
def calculate_ngram_probabilities(text, n, alpha=0.1):
    # Tokenize the input text
    tokens = word_tokenize(text)

    # Generate n-grams (with padding at sentence boundaries)
    n_grams = list(ngrams(tokens, n, pad_left=True, pad_right=True))

    # Build a frequency distribution of n-grams
    freq_dist = nltk.FreqDist(n_grams)

    # Apply Lidstone smoothing (alpha is the smoothing parameter)
    ngram_model = nltk.probability.LidstoneProbDist(freq_dist, alpha)

    # Return the probability model
    return ngram_model

# Example text for n-gram modeling
text = "N-gram with smoothing is used to predict the probability of a sequence of words."

# Create a bigram (2-gram) probability model
ngram_model = calculate_ngram_probabilities(text, 2, alpha=0.1)

# Display probability of a specific bigram ('sequence', 'of')
print("===== N-gram smoothing =====")
print(f"\nProbability of the bigram ('sequence', 'of') : ",ngram_model.prob(('sequence', 'of')))

# ----------------- Step 4: CHUNKING (Shallow Parsing) -----------------
def chunking(sentence):
    # Tokenize the input sentence
    words = word_tokenize(sentence)

    # Perform POS tagging
    pos_tags = pos_tag(words)

    # Define a simple chunk grammar rule (NP = optional determiner (DT), followed by any adjectives (JJ), ending with a noun (NN))
    chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

    # Create a chunk parser using the defined grammar
    chunk_parser = RegexpParser(chunk_grammar)

    # Parse the sentence based on grammar
    tree = chunk_parser.parse(pos_tags)

    # Return the chunk tree
    return tree

# Example sentence for chunking
sentence = "Natural Language Processing helps in understanding human language."

# Perform chunking
result_chunking = chunking(sentence)

# Display the chunking result (tree structure)
print("\n===== Chunking Result=====\n\n", result_chunking)
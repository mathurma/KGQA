# Preliminary SPO extractor

# Input: utterance
# Output: SPO of utterance

# We will assume we are given just 1 sentence
#   future development should determine what to do
#   when the utterance consistes of multiple sentences.
#   This could be as simple as identifying the sentece with '?'
#   as the target, or as complicated as resolveing coreferences
#   across tehe input sentences.

import spacy
nlp = spacy.load("en_core_web_sm")

# Parse Input
do2c = nlp("Where was Al Smith born?")
doc = nlp("Do plants feel pain?")

# Extract sentence from input
sentences = doc.sents
sentences = list(sentences) # convert generator to list

# There should only be 1 sentence in the input
if len(sentences) > 1:
    raise ValueError("Input is longer than 1 setnence.")
elif len(sentences) == 0:
    raise ValueError("Input has 0 sentences.")
sentence = sentences[0]

# Search parse tree for SPO
root = sentence.root
for child in root.children:
    print(child, child.dep_)

# Show parse tree
# spacy.displacy.serve(doc, style="dep")
# spacy.displacy.serve(do2c, style="dep")


from subject_verb_object_extract import findSVOs, nlp
str1 = "Where are the bathrooms?"

tokens1 = nlp(str1)
svos1 = findSVOs(tokens1)
print("\n1")
print(str1)
print(svos1)
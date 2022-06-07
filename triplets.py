"""
This module contains functions that extract potential triplet terms from a question.

All functions accept a question as input.
    Each question is assumed to be a single sentece only (according to spacy).
All functions return a list containing terms from the input that likely belong in a triple.
    This means that each term in the list could be either a subject, predicate, or object.
    List length is not guaranteed.

Functions:

    named_ents_and_pos(str) -> list[str]
    enhancedSVO(str) -> list[str]
    nltk_pos(str) -> list[str]
"""


def named_ents_and_pos(question):

    import spacy
    nlp = spacy.load("en_core_web_sm")

    triplets = set()

    # Process text
    doc = nlp(question)

    # Isolate sentence
    sentences = doc.sents
    sentences = list(sentences) # convert generator to list
    sentence = sentences[0]

    # Extract named entities
    for ent in doc.ents:
        triplets.add(ent.text)

    # Extract non-entities
    def _tree(tok, pos):
        if tok.dep_ in pos:
            yield tok.text
        for tok in tok.children:
            yield from _tree(tok, pos)
    for term in _tree(sentence.root, ['nsubj','dobj']):
        triplets.add(term)

    return list(triplets)

def enhancedSVO(question):
    from subject_verb_object_extract import findSVOs, nlp
    doc = nlp(question)
    return findSVOs(doc)

def nltk_pos(question):
    import nltk
    triplet = set()
    pos = ["N", "V"]
    doc = nltk.word_tokenize(question)
    pos_tagged = nltk.pos_tag(doc)
    for term, tag in pos_tagged:
        for pos in pos:
            if pos in tag:
                triplet.add(term)
    return list(triplet)

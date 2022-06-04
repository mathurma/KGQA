"""
This module contains functions that assess the similarity of two terms.

All functions accept a term and a target to match that term with/against.
All functions return a score representing how similar the term is to the target.
    Identical terms have a score of 1.
    Dissimilar terms tend to 0.

Functions:

    lenient_match(str, str) -> float
    strict_match(str, str) -> float
    spacy_sim(str, str) -> float
"""
# all methods of similarities return a value from 0 - 1, where 0 is different and 1 is similar

def lenient_match(term, target):
    from difflib import SequenceMatcher
    sm = SequenceMatcher(None, term, target)
    return sm.ratio()

def strict_match(term, target):
    if term.lower() == target.lower():
        return 1
    else:
        return 0

def spacy_sim(term, target):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    toks = nlp(term + " " + target)
    term, target = toks[0], toks[1]
    return target.similarity(term)
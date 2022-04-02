# TODO standard for organizing import statements
import en_core_web_sm
from collections.abc import Iterable

from sys import argv

from subject_verb_object_extract import findSVOs
from question_statement_convert import toStatement, isQuestion

# use spacy small model
nlp = en_core_web_sm.load()  # TODO find best way to have single nlp accessible by many files with hierarchy


if __name__ == '__main__':

    if len(argv) < 2:
        exit()
    
    doc = nlp(argv[1])
    sents = doc.sents
    sents = list(sents) # convert generator to list

    # there should only be 1 sentence in the input
    if len(sents) > 1:
        raise ValueError("Input is longer than 1 setnence.")
    elif len(sents) == 0:
        raise ValueError("Input has 0 sentences.")
    sent = sents[0]
    sentext = sent.text

    # questions need to be converted to statements
    if isQuestion(sentext):
        # TODO pass to question to statement converter
        # sent = toStatement(sent, nlp)
        pass

    svos = findSVOs(sent)

    # formulate and execute query
    # TODO where does query resolution logic go

    print("Placeholder answer.")
    
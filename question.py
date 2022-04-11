import en_core_web_sm
from subject_verb_object_extract import findSVOs

class Question(object):

    nlp =  en_core_web_sm.load()

    def __init__(self, question):
        self.question = question
        self.subject = self.predicate = self.object = ""
        if self._sentence_count() != 1:
            raise ValueError("Question is not one sentence.")
        if not self._is_question():
            raise ValueError("Question does not end with question mark.")

    # TODO - lookintuit.
    # def __del__(self):
    #     pass

    def _sentence_count(self):
        doc = Question.nlp(self.question)
        sents = doc.sents
        sents = list(sents) # convert generator to list
        return len(sents)

    def _is_question(self):
        return self.question[-1] == '?'

    def parse(self):
        doc = Question.nlp(self.question) 
        svo = findSVOs(doc)[0]
        self.subject = svo[0]
        self.predicate = svo[1]
        self.object = svo[2]

import en_core_web_sm
import re
import codec
import triplets


class Question(object):

    nlp =  en_core_web_sm.load()

    def __init__(self, question):
        self.question = question
        self.type = None
        self.triplet = None
        self.subject = self.predicate = self.object = ""
        if self._sentence_count() != 1:
            raise ValueError("Question is not one sentence.")
        if not self._is_question():
            raise ValueError("Question does not end with question mark.")

    def _sentence_count(self):
        doc = Question.nlp(self.question)
        sents = doc.sents
        sents = list(sents) # convert generator to list
        return len(sents)

    def _is_question(self):
        return self.question[-1] == '?'

    def label(self):
        for pattern in codec.QN_TYPES:
            if re.search(pattern, self.question):
                self.type = codec.QN_TYPES[pattern]
                return
        raise(TypeError("Question type cannot be identified"))

    def parse(self):
        # Interchange which triplet retrieval method is used
        self.triplet = triplets.named_ents_and_pos(self.question)

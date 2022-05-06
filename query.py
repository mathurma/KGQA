import rdflib
import en_core_web_sm

class _Similarity(object):

    nlp =  en_core_web_sm.load()

    def sim(self, w1, w2, method=1):
        if method == 1:
            return self._sim1(w1, w2)
        # elif method == N:
        #     return self._simN(w1, w2)

    def _sim1(self, w1, w2):
        toks = _Similarity.nlp(w1 + " " + w2)
        tok1, tok2 = toks[0], toks[1]
        return tok1.similarity(tok2)

    # def _simN(self, w1, w2):
    #     pass

class Query(object):

    def __init__(self, question):
        self.query = None
        self.graph = rdflib.Graph()
        self.question = question

    def parse(self, path):
       self.graph.parse(path)

    def link(self):
        # if conditions are met:
            # determine eligible subject from graph
            # determine eligible predicate from graph
            # determine eligible object from graph
        pass

import rdflib


class Answer(object):

    def __init__(self, query):
        self.query = query
        self.answer = ""

    def fill(self):
        pass

    def fix(self):
        pass

    def tmp_ans(self):
        results = []
        for row in self.query.result:
            sep = " "
            row = sep.join(row)
            results.append(row)
        sep = "\n"
        self.answer = sep.join(results)

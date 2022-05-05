import rdflib

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

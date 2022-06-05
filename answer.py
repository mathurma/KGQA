"""
This module contains resources for the answer phase.
The aswer phase is responsible for:
    - organize SPOs from a query result into a logical format based on the input question type
    - correcting the grammar within this format to yield a human-like answer

Classes:

    Answer
"""


class Answer(object):

    def __init__(self, query):
        self.query = query
        self.answer = ""

    def fill(self):
        pass

    def fix(self):
        pass

    # NOTE: to be removed after functionality for the above is implemented
    def tmp_ans(self):
        results = []
        for row in self.query.result:
            sep = " "
            row = sep.join(row)
            results.append(row)
        sep = "\n"
        self.answer = sep.join(results)

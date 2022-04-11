import unittest

from question import Question
from subject_verb_object_extract import findSVOs, printDeps, nlp

class TestQuestion(unittest.TestCase):

    def test_init(self):

        pass


class SubjectVerbOjectExtractTest(unittest.TestCase):

    def test_svo_1(self):
        tok = nlp("Where is the nearest bathroom?")
        svos = findSVOs()
        # printDeps(tok)


if __name__ == "__main__":
    unittest.main()
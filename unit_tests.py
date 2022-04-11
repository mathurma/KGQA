import unittest

from question import Question
from subject_verb_object_extract import findSVOs, printDeps, nlp

class TestQuestion(unittest.TestCase):

    def test_init_bad_question(self):
        self.assertRaises(ValueError, Question, "Not a question.") 

    def test_init_too_many_sents(self):
        self.assertRaises(ValueError, Question, "A question. But will it pass?") 

    def test_init_question(self):
        question = Question("What is a youth?")
        self.assertEqual("What is a youth?", question.question)

    def test_init_svo(self):
        question = Question("What is a youth?")
        self.assertEqual(["", "", ""], [question.subject, question.predicate, question.object])


class SubjectVerbOjectExtractTest(unittest.TestCase):

    def test_svo_1(self):
        tok = nlp("Al Smith was born in 1942.")
        printDeps(tok)
        svos = findSVOs(tok)
        print("SVOS:", svos)

if __name__ == "__main__":
    unittest.main()
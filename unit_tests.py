import unittest
import rdflib

from query import _Similarity
from question import Question
from subject_verb_object_extract import findSVOs, printDeps, nlp

class TestURI(unittest.TestCase):

    def test_SPR(self):
        g = rdflib.Graph()
        g.parse("https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPR.ttl", format="turtle")
        spr_namespace = ('spr', rdflib.term.URIRef('https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPR.ttl'))
        self.assertTrue(spr_namespace in g.namespaces)

    def test_SPRK(self):
        g = rdflib.Graph()
        g.parse("https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl", format="turtle")
        sprk_namespace = ('sprk', rdflib.term.URIRef('https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl'))
        self.assertTrue(sprk_namespace in g.namespaces)


class TestSimilarity(unittest.TestCase):

    def test_sim1_true_pos(self):
        sim = _Similarity()
        score = sim.sim("same", "different", method=1)
        print("LOOK HERE", score)
        self.assertEqual(1, score)

    def test_sim1_false_pos(self):
        sim = _Similarity()
        score = sim.sim(str(None), str(None), method=1)
        self.assertEqual(0, score)

    # Template
    # def test_simN(self):
        # sim = _Similarity()
        # score = sim.sim.sim(w1=S1, w2=S2, method=N)
        # self.assertEqual(X, score)


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
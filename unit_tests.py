import unittest
import rdflib

from question import Question
from query import Query
# from answer import Answer
from triplets import named_ents_and_pos

class TestTriplets(unittest.TestCase):

    def test_named_ents_and_pos_1(self):
        question = "What is the address of Swanton Pacific Ranch?"
        triplet = named_ents_and_pos(question)
        self.assertCountEqual(['Swanton Pacific Ranch', 'address'], triplet)

    def test_named_ents_and_pos_2(self):
        question = "When is Al Smith's birthday?"
        triplet = named_ents_and_pos(question)
        self.assertCountEqual(["Al Smith's", 'birthday'], triplet)

    # def test_named_ents_and_pos_3(self):
    #     question = "Where was Al Smith born?"
    #     triplet = named_ents_and_pos(question)
    #     self.assertCountEqual(["Al Smith", 'born'], triplet)

class TestURI(unittest.TestCase):

    def test_parse_SPR(self):
        g = rdflib.Graph()
        g.parse("https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPR.ttl", format="turtle")
        spr_namespace = ('spr', rdflib.term.URIRef('https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPR.ttl'))
        self.assertIn(spr_namespace, g.namespaces())

    def test_parse_SPRK(self):
        g = rdflib.Graph()
        g.parse("https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl", format="turtle")
        sprk_namespace = ('sprk', rdflib.term.URIRef('https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl'))
        self.assertIn(sprk_namespace, g.namespaces())

class TestSimilarity(unittest.TestCase):

    # def test_sim1_true_pos(self):
    #     sim = _Similarity()
    #     score = sim.sim("same", "different", method=1)
    #     self.assertEqual(1, score)

    # def test_sim1_false_pos(self):
    #     sim = _Similarity()
    #     score = sim.sim(str(None), str(None), method=1)
    #     self.assertEqual(0, score)

    # Template
    # def test_simN(self):
        # sim = _Similarity()
        # score = sim.sim.sim(w1=S1, w2=S2, method=N)
        # self.assertEqual(X, score)

    pass

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

class TestQuery(unittest.TestCase):

    def test__remove_ns_remove_all(self):
        g = rdflib.Graph()
        g.parse("resources/SPR.ttl")

        iri = 'https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPR.ttl'
        iri_no_ns = Query._remove_ns(g, iri)
        self.assertEqual("", iri_no_ns)

    def test__remove_ns_remove_some(self):
        g = rdflib.Graph()
        g.parse("resources/SPR.ttl")

        iri = 'https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPR.ttlFacility'
        iri_no_ns = Query._remove_ns(g, iri)
        self.assertEqual("Facility", iri_no_ns)

    def test__remove_ns_remove_none(self):
        g = rdflib.Graph()
        g.parse("resources/SPR.ttl")

        iri = 'http://danbri.org/foaf.rdf#'
        iri_no_ns = Query._remove_ns(g, iri)
        self.assertEqual("http://danbri.org/foaf.rdf#", iri_no_ns)

    def test__get_subjects(self):
        g = rdflib.Graph()
        g.parse("resources/SPR.ttl")

        ns = 'https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPR.ttl'
        subjects = ["", "Property", "Facility", "logo", "mbox",
                    "Organization", "Person", "Project", "age", "based_near",
                    "birthday", "coordinates", "address", "fun_fact", "homepage"]
        subjects = {ns+subj for subj in subjects}
        
        subjs = Query._get_subjects(g)
        self.assertEqual(subjects, set(subjs))

if __name__ == "__main__":
    unittest.main()
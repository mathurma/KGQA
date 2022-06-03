from cmath import inf
import rdflib
import re
import codec

from similarities import lenient_match

class Query(object):

    def __init__(self, question):
        self.graph = rdflib.Graph()
        self.question = question
        self.filler = ["?s", "?p", "?o"]
        self.query = None
        self.result = None
    
    def _remove_ns(self, graph: rdflib.Graph, iri: str):
        for prefix, namespace in graph.namespaces():
            namespace = namespace.toPython()
            if namespace in iri:
                return iri.replace(namespace, "")
        return iri

    def _get_subjects(self, graph: rdflib.Graph):
        subjs = list({subj for subj, pred, obj in graph}) # a list of rdflib.URIrefs
        subjs = [subj.toPython() for subj in subjs]
        subjs.sort()
        return subjs

    def _get_predicates(self, graph: rdflib.Graph):
        preds = list({pred for subj, pred, obj in graph}) # a list of rdflib.URIrefs
        preds = [pred.toPython() for pred in preds]
        preds.sort()
        return preds

    def _get_predicates(self, graph: rdflib.Graph):
        objs = list({obj for subj, pred, obj in graph}) # a list of rdflib.URIrefs
        objs = [obj.toPython() for obj in objs]
        objs.sort()
        return objs

    def parse(self, path):
       self.graph.parse(path, format="turtle")

    def link(self):
        # Interchange which similarity score algorithm is used

        # Prep dictionary
        translation = {
            "subject": None,
            "predicate": None,
            "Object": None
        }

        # Gather SPO from graph
        subjects = self._get_subjects(self.graph)
        subjects = [self._remove_ns(self.graph, subj) for subj in subjects]
        predicates = self._get_predicates(self.graph)
        predicates = [self._remove_ns(self.graph, pred) for pred in predicates]
        objects = self._get_predicates(self.graph)
        objects = [self._remove_ns(self.graph, obj) for obj in objects]

        for item in self.question.triplet:
            max_subj, subj = -inf, ""
            max_pred, pred = -inf, ""
            max_obj, obj = -inf, ""

            for subject in subjects:
                subj_sc = lenient_match(item, subject)
                t = subj_sc, subject
                c = subj_sc > max_subj
                f = max_subj, subj
                max_subj, subj = t if c else f
            
            for predicate in predicates:
                pred_sc = lenient_match(item, predicate)
                t = pred_sc, predicate
                c = pred_sc > max_subj
                f = max_pred, pred
                max_pred, pred = t if c else f

            for object in objects:
                obj_sc = lenient_match(item, object)
                t = obj_sc, object
                c = obj_sc > max_obj
                f = max_obj, obj
                max_obj, obj = t if c else f

            if max_subj > max_pred and max_subj > max_obj:
                translation["subject"] = subj
            elif max_pred > max_subj and max_pred > max_obj:
                translation["predicate"] = pred
            elif max_obj > max_subj and max_obj > max_pred:
                translation["object"] = obj

        self.filler[0] = translation["subject"] if translation["subject"] else self.filler[0]
        self.filler[1] = translation["object"] if translation["object"] else self.filler[1]
        self.filler[2] = translation["predicate"] if translation["predicate"] else self.filler[2]

        # PSEUDO
        # for each triplet:
        #   for each subject from graph:
        #       compare sim and store highest
        #   for each predicate from graph:
        #       compare sim and store highest
        #   for each object form graph:
        #       compare sim and store highest
        #   select highest of subject, predicate, object
        # 
        # if missing s p or o
        #   replace with placeholder
        # 
        # for blank s p or o in query
        #   substitute appropriate triplet

        pass


    def fill(self):
        QN = self.question.type()
        self.query = codec.QY_TYPES[QN]

        self.query = self.query % (self.filler[0], self.filler[1], self.filler[2])

        # s = "sprk:AlSmith"
        # p = "spr:birthday"
        # query = wh_query % (s, p)


        # if conditions are met:
            # determine eligible subject from graph
            # determine eligible predicate from graph
            # determine eligible object from graph
        

    def run(self):
        self.result = self.graph.query(self.query)
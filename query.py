from cmath import inf
import rdflib
import re
import codec

from similarities import lenient_match


def _get_pos(graph: rdflib.Graph, pos_idx):
    poss = list({triple[pos_idx] for triple in graph}) # a list of rdflib.URIrefs
    poss = [pos.n3(graph.namespace_manager) for pos in poss]
    return poss

def _rm_prfx(n3: str):
    idx = n3.find(':')
    if idx >= 0:
        return n3[idx+1::]
    else:
        return n3

class Query(object):

    def __init__(self, question):
        self.graph = rdflib.Graph()
        self.question = question
        self.filler = ["?s", "?p", "?o"]
        self.query = None
        self.result = None

    def parse(self, path):
       self.graph.parse(path, format="turtle")

    def link(self):
        # Interchange which similarity score algorithm is used

        # Prep dictionary
        translation = {
            "subject": None,
            "predicate": None,
            "object": None
        }

        subjects = _get_pos(self.graph, 0)
        predicates = _get_pos(self.graph, 1)
        objects = _get_pos(self.graph, 2)


        for item in self.question.triplet:
            max_subj, subj = -inf, ""
            max_pred, pred = -inf, ""
            max_obj, obj = -inf, ""

            for subject in subjects:
                subj_sc = lenient_match(item, _rm_prfx(subject))
                t = subj_sc, subject
                c = subj_sc > max_subj
                f = max_subj, subj
                max_subj, subj = t if c else f
            
            for predicate in predicates:
                pred_sc = lenient_match(item, _rm_prfx(predicate))
                t = pred_sc, predicate
                c = pred_sc > max_subj
                f = max_pred, pred
                max_pred, pred = t if c else f

            for object in objects:
                obj_sc = lenient_match(item, _rm_prfx(object))
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
        self.filler[1] = translation["predicate"] if translation["predicate"] else self.filler[1]
        self.filler[2] = translation["object"] if translation["object"] else self.filler[2]


    def fill(self):
        QN = self.question.type
        self.query = codec.QY_TYPES[QN]

        self.query = self.query % (self.filler[0], self.filler[1], self.filler[2])

        
    def run(self):
        self.result = self.graph.query(self.query)
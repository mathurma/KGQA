"""
This module contains mappings between the Question, Query, and Answer classes.
These mappings define:
    - how input is classified as a question
    - how a question is translated into a query
    - how a query informs the format of an answer

Variables: 

    QN_TYPES: Dict[regex, str]
    QY_TYPES: Dict[str, format_str]
    AN_TYPES: Dict[str, format_str]
"""


QN_TYPES = {
    "^[tT]ell me *":"direct",               # there may be many answers (objects)
    "^[wW]hat is * *":"unique_direct",      # there is only one possible answer (object)
    "^[wW]hat * about *":"listing",         # a general inquiry with many answers (subj. pred. ob.)
}

QY_TYPES = {
    "direct":""" SELECT ?o WHERE { %s %s %s . }""",
    "unique_direct":""" SELECT ?o WHERE { %s %s %s . }""",
    "listing":""" SELECT ?s ?p ?o WHERE { %s %s %s . }""",
}

# NOTE: not yet implemented
AN_TYPES = {
    "whis":"",
    "dir":""
}

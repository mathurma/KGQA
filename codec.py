

QN_TYPES = {
    "^[tT]ell me *":"direct",               # there may be many answers (objects)
    "^[wW]hat is * *":"unique_direct",      # there is only one possible answer (object)
    "^[wW]hat * about *":"listing",             # a general inquiry with many answers (subj. pred. ob.)
}

QY_TYPES = {
    "direct":""" SELECT ?o WHERE { %s %s %s . }""",
    "unique_direct":""" SELECT ?o WHERE { %s %s %s . }""",
    "listing":""" SELECT ?s ?p ?o WHERE { %s %s %s . }""",
}

AN_TYPES = {
    "whis":"",
    "dir":""
}

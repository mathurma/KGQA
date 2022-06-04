# maps
# fillers
# forms

# WHIS = "w"

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


# determine s p o
# if no one of s p o replace with ""

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
#   
# 

# QN_TYPES = ["list", "object", "query"]
# QN_TYPES = {
#     "whar": 
# }


# QN_to_QR = {
#     "S" : """ SELECT ?o WHERE { %s %s ?o . } """,
#     "list" : """ """,
# }
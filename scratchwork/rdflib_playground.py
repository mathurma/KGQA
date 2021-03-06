import turtle
import rdflib


# Try to build an RDF doc
def try_to_build():
    from rdflib import Namespace

    # This is very useful for schemas where all properties and classes have the same URI prefix.
    swanton_persons = Namespace("http://example.org/swanton_persons/")
    # TODO does n = Namespace("http://example.org/Swanton/People/") work?

    swanton_persons.alSmith  # == rdflib.term.URIRef("http://example.org/swanton_persons/alSmith")
    swanton_persons.marySmith  # == rdflib.term.URIRef("http://example.org/swanton_persons/marySmith")

    # RDFLib defines Namespaces for some common RDF/OWL schemas, including most W3C ones:
    from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                            PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                            VOID, XMLNS, XSD

    from rdflib import Graph, URIRef, Literal, BNode
    from rdflib.namespace import FOAF, RDF

    g = Graph()
    g.bind("foaf", FOAF)

    bob = URIRef("http://example.org/people/Bob")
    linda = BNode()  # a GUID is generated

    name = Literal("Bob")
    age = Literal(24)

    g.add((bob, RDF.type, FOAF.Person))
    g.add((bob, FOAF.name, name))
    g.add((bob, FOAF.age, age))
    g.add((bob, FOAF.knows, linda))
    g.add((linda, RDF.type, FOAF.Person))
    g.add((linda, FOAF.name, Literal("Linda")))

def try_to_build_demo():
    from rdflib import Graph, URIRef, Literal, BNode
    from rdflib.namespace import FOAF, RDF

    g = Graph()
    g.bind("foaf", FOAF)

    bob = URIRef("http://example.org/people/Bob")
    linda = BNode()  # a GUID is generated

    name = Literal("Bob")
    age = Literal(24)

    g.add((bob, RDF.type, FOAF.Person))
    g.add((bob, FOAF.name, name))
    g.add((bob, FOAF.age, age))
    g.add((bob, FOAF.knows, linda))
    g.add((linda, RDF.type, FOAF.Person))
    g.add((linda, FOAF.name, Literal("Linda")))

    print(g.serialize())    

def try_to_build_custom():
    from rdflib import Namespace, Graph
    n = Namespace("http://example.org/swanton/people/") # must end with '/'
    AlSmith = n.AlSmith  # == rdflib.term.URIRef("http://example.org/Swanton/People/AlSmith")
    StanleySmith = n.StanleySmith  # == rdflib.term.URIRef("http://example.org/Swanton/People/StanleySmith")
    LorenSmith = n.LorenSmith  # == rdflib.term.URIRef("http://example.org/Swanton/People/LorenSmith")

    g = Graph()
    g.bind("spr/people", n)

    g.add((AlSmith, n.SonOf, StanleySmith))
    g.add((LorenSmith, n.SonOf, StanleySmith))

    print(g.serialize())
    g.serialize("SwantonPeople")  # save to file, defaults to TTL forrmat

# Try to pull all S || V || O from an RDF doc
def try_to_pull():
    # str() method?
    predicate_query = """
    SELECT DISTINCT ?p
    WHERE {
        ?s ?p ?o .
    }
    ORDER BY ?p"""

    g = rdflib.Graph()
    g.parse("data/foaf.rdf")
    qres = g.query(predicate_query)
    for row in qres:
        print(row.p)

def extended_example():
    # Load existing RDF file in wrong/ugly format (XML)
    # Pull all it's predicates with RDFLib and not SPARQL Query
    # Serialize to new RDF file in proper format (TTL)

    g = rdflib.Graph()
    g.parse("data/foaf.rdf")

    preds = list({ pred.n3(g.namespace_manager) # n3 format to afix with prefix (simplify output)
        for subj, pred, obj in g})
    preds.sort()
    print(*preds, sep='\n')

    g.serialize("data/foaf.ttl")


# Try to query an RDF doc
def try_to_query():
    g = rdflib.Graph()  # have to make the graph object first

    # Two parse styles:
    g.parse("http://danbri.org/foaf.rdf#")  # readily avialable online
    g.parse("data/foaf.rdf")  # saved locally

    knows_query = """
    SELECT DISTINCT ?aname ?bname
    WHERE {
        ?a foaf:knows ?b .
        ?a foaf:name ?aname .
        ?b foaf:name ?bname .
    }"""

    qres = g.query(knows_query)
    for row in qres:
        print(f"{row.aname} knows {row.bname}")

def try_custom_import():
    # import SPR_FOAF
    from rdflib.namespace import RDF, SPR
    from rdflib import Graph, URIRef, Literal, BNode
    from rdflib.namespace import Namespace

    # SPR_FOAF = Namespace(SPR_FOAF)
    # type(RDF)(SPR_FOAF)
    print("RDF:", type(RDF))
    print("SPR:", type(SPR))

    g = Graph()
    # g.parse(SPR)
    g.bind("SPR", SPR)

    orchard = URIRef("https://swantonpoppycp.github.io/CalPoppy/SPR/KG/UPickAppleOrchard")
    address = Literal("123 San Simeon, CA 9000")

    g.add((orchard, RDF.type, SPR.Agent))
    # g.add((orchard, SPR.address, SPR_FOAF.Property))
    # print(g.serialize())

def build_spr():
    from rdflib.namespace import SPR, RDF
    from rdflib import Graph, URIRef, Literal, BNode
    from rdflib.namespace import Namespace

    g = Graph()
    g.bind("spr", SPR)

    al_smith = Literal("Al Smith")  # a GUID is generated
    blank = BNode()
    al_smith = blank

    g.add((al_smith, RDF.type, SPR.Person))
    # g.add((al_smith, SPR.alias, Literal("Albert B. Smith"))) # term not in SPR - breaks appropriately
    g.add((al_smith, SPR.fun_fact, Literal("Did you know? Al Smith lost his leg in a train accident in 1945.")))

    g.serialize("SPR_data-default") 
    g.serialize("SPR_data-turtle", format='turtle') 
    g.serialize("SPR_data-turtle", format='n3') 



def  test_q_types():
    import rdflib
    g = rdflib.Graph()
    g.parse("http://danbri.org/foaf.rdf#")

    knows_query = """
    SELECT DISTINCT ?aname ?bname ?a ?b
    WHERE {
        ?a foaf:knows ?b .
        ?a foaf:name ?aname .
        ?b foaf:name ?bname .
    }"""

    qres = g.query(knows_query)
    for row in qres:
        print(f"{row.aname} knows {row.bname}, where {row.aname}'s source is {row.a} and {row.bname}'s source is {row.b}")
        break


def test_uri():
    import rdflib
    # from rdflib.namespace import SPR, RDF, FOAF

    g = rdflib.Graph()
    # g.parse("SPR_data")
    # g.parse("http://raw.githubusercontent.com/mathurma/KGQA/main/data/foaf.rdf")
    # g.parse("http://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl", format='text/plain')
    # g.parse("http://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl", format='turtle') # format = ...turtle, n3, text/turtle
    # g.parse("http://danbri.org/foaf.rdf#")

    # Possible formats: "turtle" == "text/turtle" != "n3"
    #   default format is "application/rdf+xml" (see URLInputSource)

    # Works
    def works():
        g.parse("resources/SPRK.ttl", format="turtle"),
        g.parse("resources/SPRK.ttl"), # <- detects format as ttl with rdflib.util.guess_format bc (create)input_source had attribute 'file'
            # create_input_source <- create_input_source_from_location(file) <- location(None) <- source(str) 
        g.parse("http://danbri.org/foaf.rdf#"),  # defaults to rdf format, performs URL request with format as header and gets content type (for parsing) from file info
            # create_input_source <- create_input_source_from_location(URLinput) <- location(None) <- source(str) 
        g.parse("http://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl", format="turtle")


    # Fails
    def fails():
        g.parse("http://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl")
            # graphy.py:1255 - parser = plugin.get(format:'text/plain' , Parser) <== DNE
    
    g.parse("http://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPR.ttl", format="turtle")


def test_q_types_f_spr():
    import rdflib
    g = rdflib.Graph()
    g.parse("https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl", format="turtle")

    all_query = """ SELECT DISTINCT ?s ?p ?o WHERE { ?s ?p ?o . } """
    wh_query = """ SELECT DISTINCT ?o WHERE { %s %s ?o . } """
    s = "sprk:AlSmith"
    p = "spr:birthday"
    query = wh_query % (s, p)

    qres = g.query(query)
    x = 0
    for row in qres:
        print(x, row.o)
        x += 1

def test_q_types_f_spr():
    import rdflib
    g = rdflib.Graph()
    print("pre")
    # print(g.base)
    # print(g.identifier)
    # print([namespace for namespace in g.namespaces()])
    g.parse("https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl#", format="turtle")
    print("post")
    # print(g.base)
    # print(g.identifier)
    # print([namespace for namespace in g.namespaces()])

    qres = g.query(' SELECT ?o WHERE { sprk:AlSmith spr:fun_fact ?o . } ')
    for row in qres:
        print(row)


    # all_query = """ SELECT DISTINCT ?s ?p ?o WHERE { ?s ?p ?o . } """
    # wh_query = """ SELECT DISTINCT ?o WHERE { %s %s ?o . } """
    # s = "sprk:AlSmith"
    # p = "spr:birthday"
    # query = wh_query % (s, p)

    # qres = g.query(all_query)
    # x = 0
    # for row in qres:
    #     print(x, row.s, row.p, row.o, "row:", row)
    #     x += 1

def test_pull_prefixes():
    g = rdflib.Graph()
    g.parse("https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl#", format="turtle")

    l = []
    for s, p, o in g:
        print(s, type(s), s.n3(g.namespace_manager))
        print(p, type(p), p.n3(g.namespace_manager))
        print(o, type(o), o.n3(g.namespace_manager))

    for ns in g.namespaces():
        print(ns)

    # rdf=rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    # rdflib.term.URIRef(rdf+'type')    
    # rdflib.term.URIRef(rdf['type'])
    
    pass

def test_get_str_from_res():
    import rdflib

    # def _rdfterm_to_str(term):
    #     if type(term) is rdflib.term.Literal:
    #         return term.value()
    #     elif type(term) is rdflib.term.URIRef:
    #         return term.



    def _pos_prfx(graph: rdflib.Graph, poss):
        return [pos.n3(graph.namespace_manager) for pos in poss]

    def _get_pos(graph: rdflib.Graph, pos_idx):
        poss = list({triple[pos_idx] for triple in graph}) # a list of rdflib.URIrefs
        poss = _pos_prfx(graph, poss)
        return poss

    def _rm_prfx(n3: str):
        idx = n3.find(':')
        if idx >= 0:
            return n3[idx+1::]
        else:
            return n3


    g = rdflib.Graph()
    g.parse("https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl#", format="turtle")

    all_query = """ SELECT DISTINCT ?s ?p ?o WHERE { ?s ?p ?o . } """

    qres = g.query(all_query)
    for row in qres:
        print(row)
        print(type(row)) # rdflib.query.ResultRow
        srow = _pos_prfx(g, list(row))
        # srow = [item.n3(graph.namespace_manager) for item in row]
        # srow_np = [item.]
        srow_np = [_rm_prfx(item) for item in srow]
        for item in row:
            print(item)
            print(type(item))
            sitem = item.n3(g.namespace_manager)
            # itm

test_get_str_from_res()
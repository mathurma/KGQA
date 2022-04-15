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

try_custom_import()
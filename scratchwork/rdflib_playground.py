import rdflib


# Try to build an RDF doc
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

                        

# Try to pull all S || V || O from an RDF doc


# Try to query and RDF doc

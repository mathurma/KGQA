from rdflib.term import URIRef
from rdflib.namespace import DefinedNamespace, Namespace


class SPR(DefinedNamespace):
    """
    Swanton Pacific Ranch (SPR) vocabulary

    The Swanton Pacific Ranch RDF vocabulary, described using W3C RDF Schema and the Web Ontology Language.

    Generated from: https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPR.ttl
    Date: 2022-04-14

    """

    _fail = True

    # http://www.w3.org/1999/02/22-rdf-syntax-ns#Property
    # Predicates
    age: URIRef  # The age in years of some agent.
    based_near: URIRef  # A location that something is based near, for some broadly human notion of near.
    birthday: URIRef  # The birthday of this Person, represented in mm-dd string form, eg. '12-31'.
    coordinates: URIRef  # GPS coordinates.
    address: URIRef  # A physical mailing address.
    fun_fact: URIRef  # An interesting and niche tidbit about a Person.

    # http://www.w3.org/2000/01/rdf-schema#Class
    # Subjects or objects
    Property: URIRef # A designated, natural land or space on the ranch.
    Facility: URIRef # A building or man-made structure on the ranch.
    Organization: URIRef  # An organization.
    Person: URIRef  # A person.
    Project: URIRef  # A collective endeavour of some kind.

    # http://www.w3.org/2002/07/owl#InverseFunctionalProperty
    # A type of property that can only have once instance per subject (?)
    homepage: URIRef  # A homepage for some thing.
    logo: URIRef  # A logo representing some thing.
    mbox: URIRef  # A personal mailbox, ie. an Internet mailbox associated with exactly one owner.

    _NS = Namespace("https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPR.ttl")  # https://xmlns.com/FOAF/0.1/ links to https://xmlns.com/FOAF/spec/

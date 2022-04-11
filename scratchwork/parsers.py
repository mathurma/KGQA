# How do each of the major open source parsers handle questions?

################################################################################
# Spacy
import spacy
from nltk.tree import Tree

spacy_nlp = spacy.load("en_core_web_sm")


def nltk_spacy_tree(sent):
    """
    Visualize the SpaCy dependency tree with nltk.tree
    """
    doc = spacy_nlp(sent)
    def token_format(token):
        return "_".join([token.orth_, token.tag_, token.dep_])

    def to_nltk_tree(node):
        if node.n_lefts + node.n_rights > 0:
            return Tree(node,
                       [to_nltk_tree(child) 
                        for child in node.children]
                   )
        else:
            return node

    tree = [to_nltk_tree(sent.root) for sent in doc.sents]
    # The first item in the list is the full tree
    tree[0].draw()

nltk_spacy_tree("When was Al Smith was born?")

################################################################################
# NLTK

################################################################################
# OpenNLP


################################################################################
# Stanford
from nltk.tree import Tree
from nltk.parse.stanford import StanfordParser

# Note: Download Stanford jar dependencies first
# See https://stackoverflow.com/questions/13883277/stanford-parser-and-nltk
stanford_parser = StanfordParser(
    model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz"
)

def nltk_stanford_tree(sent):
    """
    Visualize the Stanford dependency tree with nltk.tree
    """
    parse = stanford_parser.raw_parse(sent)
    tree = list(parse)
    # The first item in the list is the full tree
    tree[0].draw()
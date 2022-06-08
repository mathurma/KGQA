"""
This is the primary module of KGQA, and it links functionality from the query, question, and answer phases
    in order to output an answer to an input question, based on information from a knowledge graph.

Fuctions:

    main(str) -> str
"""


from sys import argv

from question import Question
from query import Query
from answer import Answer


def main(input):

    try:
        # Question Phase
        qn = Question(input)  # create question
        qn.parse()  # parse SPO
        qn.label()  # label question type

        # Query Phase
        qy = Query(qn)  # create query
        qy.parse("https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl#")  # parse graph
        qy.link()  # link qn-S|P|O with graph-S|P|O
        qy.fill()  # fill query template with graph-S|P|O
        qy.run()  # run query

        ## Answer Phase
        an = Answer(qy)  # create answer
        an.fill()  # fill answer template with result-S|P|O
        an.fix()  # fix grammatical errors

        # NOTE: to be removed once Answer functions above are implemented
        an.tmp_ans()

        return an.answer
    except Exception as e:
        return "ERROR: "+e


if __name__ == '__main__':
    try:
        print(main(argv[1]))
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    except Exception as e:
        print(e)

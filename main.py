from sys import argv
from question import Question
from query import Query

def main(input):
    qn = Question(input)  # create question
    qn.parse()  # parse SVO
    qn.label()  # label type


    qy = Query(qn)  # create query
    qy.parse("https://raw.githubusercontent.com/mathurma/KGQA/main/resources/SPRK.ttl#")  # parse graph
    qy.link() # link qn-S|V|O with graph-S|V|O
    qy.fill()  # fill query template with graph-S|V|O
    qy.run()  # execute query

    # an = Answer(qy)  # create answer
    # an.shape()
    # an.fix()
    # return an.answer

    return "Placeholder answer from Matthew"



if __name__ == '__main__':
    try:
        main(argv[1])
    except ValueError as ve:
        print(ve)

from sys import argv
import question, query

def main(input):
    qn = question(input)  # create question
    qn.parse()  # parse SVO

    qy = query(qn)  # create query
    # qy.parse("path of SPR graph")  # parse graph
    # qy.link()  # link qn-S|V|O with graph-S|V|O
    # qy.run()  # execute query

    # an = answer(qy)  # create answer
    # an.parse

    return "Placeholder answer from Matthew"



if __name__ == '__main__':
    try:
        main(argv)
    except ValueError as ve:
        print(ve)

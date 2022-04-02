

# is the input a WH statement?
def isWh(tokens):
    first = tokens[0].lower_
    return "who" == first or "what" == first or "when" == first or "where" == first

# does a statement end in a question mark?
def isQuestion(statement: str):
    return statement[:-1] == '?'

# preprocess input
def toStatement(input):
    pass

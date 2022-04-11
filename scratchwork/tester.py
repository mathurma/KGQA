# Point of this file:
#   import csv of questions and their corresponding SVOs
#   use a specific method/source for SVOE
#   call SVOE on each question, check if it works for SVOE
# Future features:
#   suite for SVOE
#   suite for edge cases
# Questions:
#   is this appropraite for a unit test?

import unittest

class TestProblem(unittest.TestCase):

    # TODO what is this for
    def __init__(self, methodName: str):
        unittest.TestCase.__init__(self, methodName)

    def test_sample(self):
        self.assertEqual(1, 1)

    # Test the bare mininum - SVOE results contain SVO

    # Test modifiers? SVOE contains modifiers (alone? <- up to you probably)

    #

if __name__ == '__main__':
    unittest.main()
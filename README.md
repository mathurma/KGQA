# KGQA
A brief description about this program.
 
## Reading for Understanding
- [W3C's Primer for Understanding RDF](https://www.w3.org/TR/rdf11-primer/)

- [Generalized RDF](https://www.w3.org/TR/rdf11-concepts/#section-generalized-rdf)

## Reading for Implementation
- [parsing RDF files](https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html)

## Instructions
- Import custom schema to RDFLib:
  - locate your RDFlib installation
  - place your RDFLib Namespace class file in the `rdflib/namespace` directory
  - ensure your Namespace class file references an eligible URI _(ex: `http://www.w3.org/1999/02/22-rdf-syntax-ns#`)_
- Run unit tests: `python3 -m unittest unit_tests.py`
- Run program: `python3 ....py "<question>?"`

## Requirements

## Todo
- [ ] enforce python version
- [ ] add linter
- [ ] enforce python standard

## Research
- [x] merge RDF graphs
- [x] import custom URI
- [x] create custom URI
- [x] remove namespace from URI
- [ ] check that all URI's are being used correctly
- [ ] visualize RDF graph

## References
- [1](https://stackoverflow.com/a/25200825)
- [2](https://stackoverflow.com/a/56627856)
- [3](https://stackoverflow.com/a/66114342)

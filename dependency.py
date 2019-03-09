import sys
from pycorenlp import StanfordCoreNLP
import json
from textacy import extract as ext
from textacy import Doc

def extract_triple(text):
    doc = Doc(text)
    print("\nTriples from SpaCy: ")
    for item in ext.subject_verb_object_triples(doc):
        print("\t", item)

def core_nlp_triple(text):
    print("\nTriples from CoreNLP: ")
    output = nlp.annotate(text, properties={'annotators': 'openie','outputFormat': 'json'})
    relations = [ rel for sentence in output['sentences'] for rel in sentence['openie']]
    for i in relations:
        print("\t", tuple([i['subject'], i['relation'], i['object']]))

if __name__ == '__main__':
    nlp = StanfordCoreNLP('http://localhost:9000')
    text = None
    with open(sys.argv[1], 'r') as f:
        text = f.readlines()

    for line in text:
        print("\n\n")
        print(line)
        extract_triple(line)
        core_nlp_triple(line)

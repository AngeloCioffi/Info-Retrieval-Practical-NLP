import sys
from stanfordnlp.server import CoreNLPClient
import json
from textacy import extract as ext
from textacy import Doc

def extract_triple(text):
    doc = Doc(text)
    print("\nTriples from SpaCy: ")
    for item in ext.subject_verb_object_triples(doc):
        print("\t", item)

def core_nlp_triple(text):
    with CoreNLPClient(annotators=['openie','ner','coref'], timeout=30000, memory='16G') as client:
        print("\nTriples from CoreNLP: ")
        print(client.annotate(text))

if __name__ == '__main__':
    text = None
    # with open(sys.argv[1], 'r') as f:
    #     json_data = json.loads(f.read())
    #
    # for item in json_data.values():
    #     print("\n\nArticle: ", item['title'])
    #     extract_triple(item['article'])
    #     core_nlp_triple(item['article'])
    #     input()
    var = "Amazon plans to open its first grocery store in Los Angeles as early as the end of the year, one person said. "
    print(var)
    extract_triple(var)
    core_nlp_triple(var)

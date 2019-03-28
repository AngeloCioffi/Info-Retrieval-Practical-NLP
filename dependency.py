import sys
from stanfordnlp.server import CoreNLPClient
import json
from textacy import extract as ext
from textacy import Doc

def extract_triple(text):
    doc = Doc(text, lang='en_core_web_sm')
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
    var = """
    The Week Ahead: There are some assorted conferences and investor events being held this week. Utility Sempra Energy (SRE), for instance, hosts an analyst day on Wednesday. Software maker Autodesk (ADSK) hosts one on Thursday. On the economic front, U.S. housing data hits the tape on Tuesday. This week's big event comes later, when ride-sharing company Lyft (LYFT) prices its initial public offering. Lyft plans to raise up to $2 billion, giving the entire company a valuation of about $18 to $20 billion. """
    var = var.replace("%", " percent")
    print(var)
    extract_triple(var)
    core_nlp_triple(var)

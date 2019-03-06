import sys
from pycorenlp import StanfordCoreNLP
import json

if __name__ == '__main__':
    nlp = StanfordCoreNLP('http://localhost:9000')
    text = "Amazon is buying three stores."
    print(text)
    output = nlp.annotate(text, properties={'annotators': 'openie','outputFormat': 'json'})
    print(json.dumps(output, indent=True))
    relations = [ rel for sentence in output['sentences'] for rel in sentence['openie']]
    for i in relations:
        print(tuple([i['subject'], i['relation'], i['object']]))

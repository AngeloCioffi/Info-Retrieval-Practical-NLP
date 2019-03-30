from textacy import extract as ext
from textacy import Doc
import re
import json 
import sys
import spacy
from spacy import displacy

from neo4j_test.neo4j_test import create_triple

corref = spacy.load('en_coref_md')
print("loaded coref")
def resolve_correfs(text):
    #return text #TODO
    doc = corref(text)

    #print(doc._.has_coref)
    print(doc._.coref_clusters)
    return doc._.coref_resolved

propn = "PROPN"
def span_is_interesting(item):
    return item.root.pos_ == propn

def subject_to_subtree(item):
    return ' '.join([t.text for t in item.root.subtree])

def extract_triples(text, json):
    doc = Doc(text, lang='en_core_web_sm')
    for item in ext.subject_verb_object_triples(doc):
        if span_is_interesting(item[0]) or span_is_interesting(item[2]):
            #print(item)
            exp_sub = subject_to_subtree(item[0])
            sub = ' '.join([x.text for x in item[0]])
            verb = ' '.join([x.text for x in item[1]])
            obj = ' '.join([x.text for x in item[2]])
            exp_obj = subject_to_subtree(item[2])

            sub_pn = ""
            if span_is_interesting(item[0]):
                sub_pn = sub

            obj_pn = ""
            if span_is_interesting(item[2]):
                obj_pn = obj

            print([sub_pn, exp_sub, verb, obj_pn, exp_obj])
            create_triple(json['company'], json['date'], json['url'], verb, sub_pn, exp_sub, obj_pn, exp_obj)


nlp = spacy.load("en_core_web_sm")
print("loaded web_sm")
def visualize(text):
    doc = nlp(text)
    sentence_spans = list(doc.sents)
    #displacy.serve(sentence_spans, style="ent")
    displacy.serve(sentence_spans, style="dep")

def convert_unicode_quotes(var1):
    var1 = re.sub(r'(\u201c)|(\u201d)|(\u201f)|(\u2033)|(\u2036)', "\"", var1)
    var1 = re.sub(r'(\u2018)|(\u2019)|(\u201b)|(\u2032)|(\u2035)', "\'", var1)
    var1 = var1.encode('ascii', 'ignore').decode('utf-8')
    return var1

def sanitize_string(var1):
    var1 = re.sub(r', [+-]\d+\.\d+%', "", var1) #ticker value
    var1 = re.sub(r'[Ii]nc.', "Inc", var1) #Inc sentence
    var1 = re.sub(r'\([^()]*\)', " ", var1) #perens
    var1 = re.sub(r'(\\u201c)|(\\u201d)|(\\u201f)|(\\u2033)|(\\u2036)', "\"", var1)
    var1 = re.sub(r'(\\u2018)|(\\u2019)|(\\u201b)|(\\u2032)|(\\u2035)', "\'", var1)
    var1 = re.sub(r'\\u[0-9a-f]{4}', "", var1)
#var1 = var1.replace("%", " percent")
    return var1

def process_corpus():
    with open("Scrapy/MarketWatchData.txt", 'r') as f:
        data = f.read()
        #data = convert_unicode(data)
        json_data = json.loads(data)

    count = 0
    for item in json_data:

        title = convert_unicode_quotes( item['title'] )
        article = convert_unicode_quotes( item['article'] )

        var1 = title+article
      
        count += 1
        print(count)
        print("\n\nArticle: ", title)

        var1 = sanitize_string(var1)
        #print(var1)
        var1 = resolve_correfs(var1)

        extract_triples(var1, item)


if __name__ == '__main__':
    process_corpus()

#    var1 = r'''
#    Amazon is planning to open dozens of grocery stores in several major U.S. cities, according to people familiar with the matter, as the retail giant looks to broaden its reach in the food business.'''
    #American Airlines Group Inc. AAL, +0.03% disclosed Monday that its expects the Federal Aviation Administration's grounding of Boeing Co.'s BA, +1.02% 737 MAX aircraft to continue to cause "significant disruption" to its customers and financial costs to the airline. The company said, however, that the financial costs of the disruption "cannot be forecasted at this time," as they will depend on a number of factors, including the period of time of the grounding and the circumstances related to the reintroduction of the aircraft. American said in a filing with the SEC that its fleet included 24 Boeing MAX 8 aircraft, with an additional 76 aircraft on order. Prior to the grounding, it had been operating on average about 90 flights a day involving the grounded aircraft, with flight cancellations announced through April 24, so far. American's stock slipped 0.1% in premarket trade. It has shed 4.8% year to date, while Boeing shares have rallied 12.3%, the NYSE Arca Airline Index XAL, -0.33% has gained 4.5% and the Dow Jones Industrial Average DJIA, +0.23% has advanced 9.3%.'''

#    print(var1)
#    var1 = sanitize_string(var1)
#    print("sanitized:", var1)
#    var1 = resolve_correfs(var1)
#    print("correfs:", var1)
#    extract_triples(var1, {})
    #visualize(var1)



    

import spacy
from spacy import displacy

nlp = spacy.load('en_coref_md')

print("loaded")

text = r'''
Although Apple does not break down sales of AirPods, the company reported in January that its "other" product category, which includes AirPod sales, grew 33% to $7.3 from a year earlier, the fastest growing category.'''

doc = nlp(text)

doc._.has_coref
coref = doc._.coref_clusters
resolved = doc._.coref_resolved

print(coref)
print(resolved)

displacy.serve(coref, style="ent")

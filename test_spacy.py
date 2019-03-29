import en_core_web_sm
from spacy import displacy
import re
import spacy.symbols

nlp = en_core_web_sm.load()
doc_text = """When Warren Buffett\u2019s annual letter to Berkshire Hathaway shareholders was published last weekend, media coverage focused on the chairman and CEO\u2019s mea culpaabout Berkshire\u2019s investment in Kraft Heinz KHC, -0.55% his lament that he couldn\u2019t find the next big investment to buy, the accounting change that caused Berkshire to take a $20 billion write-down, and, once again, his failure to announce any formal succession plans even though Buffett is 88 years old and Vice Chairman Charlie Munger is 95.But one thing jumped out at me in his annual letter and a subsequent extended interview with Becky Quick of CNBC: his acknowledgment that his best stock pickers hadn\u2019t beaten the market and his tacit admission that investors couldn\u2019t expect Berkshire Hathaway BRK.A, +0.02% BRK.B, -0.06%  to do so in the future, either.Todd Combs and Ted Wechsler joined Berkshire as investment managers within a year of each other in 2011-2012. \u201cOverall, they are a tiny bit behind the S&P SPX, +0.08%   each by just almost the same margin over the same time,\u201d Buffett told Quick."""

doc_text = re.sub(r', [+-]\d+\.\d+%', "", doc_text)

doc = nlp(doc_text)

# options = {"compact": True}
# displacy.serve(doc, style="dep")

for token in doc:
    if token.dep == nsubj and token.head.pos == VERB:
        verb = token.head
        triple = {}

        subject_expanded = ""
        for subject_child in token.children:
        	subj_mods = [poss, amod, compound]
        	if any(subject_child in sm for x in subj_mods):
        		subject_expanded = subject_child.text + token.text

        right_dep = [dobj, pobj, npadvmod, acomp]
        object_expanded = ""
        for right_token in verb.children:
            if any(right_token in dp for x in right_dep):
            	for child in right_token.children: #will this cause error with no children?
            		if right_token == dobj:
            			dobj_mods = [nummod, compound, nmod]
            			if any(child in dm for x in dobj_mods):
            				object_expanded = child.text + right_token.text
            		else if right_token == pobj:
            			if child == nummod:
            				object_expanded = child.text + right_token.text
            		else if right_token == acomp:
            			if child == npadvmod:
            				object_expanded = child.text + right_token.text
            	triple = [verb.text, token.text, subject_expanded, right_token.text, object_expanded]
            else if right_token == prep:
            	for child in right_token.children:
            		if child == pobj:
            			object_expanded = right_token.text + child.text 
            				triple = [verb.text, nsubj.text, right_token.text, object_expanded]

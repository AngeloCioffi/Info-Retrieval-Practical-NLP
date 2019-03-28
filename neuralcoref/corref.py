import spacy
nlp = spacy.load('en_coref_md')
text = u'The bans come after Sunday\'s Ethiopian Airlines crash, which resulted in the deaths of 157 people near Addis Ababa.  The action comes despite the U.S. Federal Aviation Administration\'s continued vouching for the safety of the plane as American authorities, Boeing and Ethiopian investigators probe the crash.'

doc = nlp(text)

doc._.has_coref
doc._.coref_clusters

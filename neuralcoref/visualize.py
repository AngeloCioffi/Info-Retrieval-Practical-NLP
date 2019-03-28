
import sys

import spacy
from spacy import displacy


if __name__ == '__main__':
    nlp = spacy.load("en_coref_md")
    #nlp = spacy.load("en_core_web_sm")
    
    var = """

    American Airlines 'cannot' forecast costs of grounding of 737 MAX aircraft because of uncertainties
    American Airlines Group Inc. AAL, +0.03% disclosed Monday that its expects the Federal Aviation Administration's grounding of Boeing Co.'s BA, +1.02% 737 MAX aircraft to continue to cause "significant disruption" to its customers and financial costs to the airline. The company said, however, that the financial costs of the disruption "cannot be forecasted at this time," as they will depend on a number of factors, including the period of time of the grounding and the circumstances related to the reintroduction of the aircraft. American said in a filing with the SEC that its fleet included 24 Boeing MAX 8 aircraft, with an additional 76 aircraft on order. Prior to the grounding, it had been operating on average about 90 flights a day involving the grounded aircraft, with flight cancellations announced through April 24, so far. American's stock slipped 0.1% in premarket trade. It has shed 4.8% year to date, while Boeing shares have rallied 12.3%, the NYSE Arca Airline Index XAL, -0.33% has gained 4.5% and the Dow Jones Industrial Average DJIA, +0.23% has advanced 9.3%."""
    var = var.replace("%", " percent")

    doc = nlp(var)
    sentence_spans = list(doc.sents)
    displacy.serve(sentence_spans, style="dep")

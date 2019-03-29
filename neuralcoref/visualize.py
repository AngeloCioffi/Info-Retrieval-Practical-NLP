
import sys
import re

import spacy
from spacy import displacy


if __name__ == '__main__':
    #nlp = spacy.load("en_coref_md")
    nlp = spacy.load("en_core_web_sm")

    var1 = """
    American Airlines 'cannot' forecast costs of grounding of 737 MAX aircraft because of uncertainties
    American Airlines Group Inc. AAL, +0.03% disclosed Monday that its expects the Federal Aviation Administration's grounding of Boeing Co.'s BA, +1.02% 737 MAX aircraft to continue to cause "significant disruption" to its customers and financial costs to the airline. The company said, however, that the financial costs of the disruption "cannot be forecasted at this time," as they will depend on a number of factors, including the period of time of the grounding and the circumstances related to the reintroduction of the aircraft. American said in a filing with the SEC that its fleet included 24 Boeing MAX 8 aircraft, with an additional 76 aircraft on order. Prior to the grounding, it had been operating on average about 90 flights a day involving the grounded aircraft, with flight cancellations announced through April 24, so far. American's stock slipped 0.1% in premarket trade. It has shed 4.8% year to date, while Boeing shares have rallied 12.3%, the NYSE Arca Airline Index XAL, -0.33% has gained 4.5% and the Dow Jones Industrial Average DJIA, +0.23% has advanced 9.3%."""


    #Las Vegas Sands LVS, -0.70% will participate in the J.P. Morgan Gaming, Lodging, Restaurant & Leisure Management Access Forum in Las Vegas, NV on Thursday, March 14, 2019. Mr. Daniel Briggs, Senior Vice President Investor Relations, will participate in a discussion which is scheduled to begin at approximately 4:05 p.m. Pacific Time (7:05 p.m. Eastern Time).A webcast of the discussion may be accessed at the Investor Relations section of the company's website at www.sands.com.  About Las Vegas Sands Corp LVS, -0.70%Las Vegas Sands is the world's pre-eminent developer and operator of world-class Integrated Resorts. We deliver unrivaled economic benefits to the communities in which we operate.LVS created the meetings, incentives, convention and exhibition (MICE)-based Integrated Resort. Our industry-leading Integrated Resorts provide substantial contributions to our host communities including growth in leisure and business tourism, sustained job creation and ongoing financial opportunities for local small and medium-sized businesses.Our properties include The Venetian and The Palazzo resorts and Sands Expo in Las Vegas, Sands Bethlehem in Eastern Pennsylvania, and the iconic Marina Bay Sands in Singapore. Through majority ownership in Sands China Ltd., we have developed the largest portfolio of properties on the Cotai Strip in Macao, including The Venetian Macao, The Plaza and Four Seasons Hotel Macao, Sands Cotai Central and The Parisian Macao, as well as the Sands Macao on the Macao Peninsula.LVS is dedicated to being a good corporate citizen, anchored by the core tenets of serving people, planet and communities.  We deliver a great working environment for 50,000 team members worldwide, drive social impact through the Sands Cares charitable giving and community engagement program and lead in environmental performance through the award-winning Sands ECO360 global sustainability program. To learn more, please visit www.sands.com.Contacts:\nInvestment Community:\nDaniel Briggs\n(702) 414-1221Media:\nRon Reese\n(702) 414-3607 View original content to download multimedia:http://www.prnewswire.com/news-releases/las-vegas-sands-to-participate-in-the-2019-jp-morgan-gaming-lodging-restaurant--leisure-management-access-forum-300812797.htmlSOURCE Las Vegas SandsCopyright (C) 2019 PR Newswire. All rights reserved", "title": "Las Vegas Sands to Participate in the 2019 J.P. Morgan Gaming, Lodging, Restaurant & Leisure Management Access Forum"""

    var1 = re.sub(r', [+-]\d+\.\d+%', "", var1)
    #var1 = var1.replace("%", " percent")

    doc = nlp(var1)
    sentence_spans = list(doc.sents)
    displacy.serve(sentence_spans, style="dep")

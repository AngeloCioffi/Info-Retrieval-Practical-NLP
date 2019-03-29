from textacy import extract as ext
from textacy import Doc
import re

import sys
import spacy
from spacy import displacy

#corref = spacy.load('en_coref_md')
print("loaded coref")
def resolve_correfs(text):
    doc = corref(text)

    print(doc._.has_coref)
    print(doc._.coref_clusters)
    return doc._.coref_resolved

def extract_triple(text):
    doc = Doc(text, lang='en_core_web_sm')
    for item in ext.subject_verb_object_triples(doc):
        print(item)

nlp = spacy.load("en_core_web_sm")
print("loaded web_sm")
def visualize(text):
    doc = nlp(text)
    sentence_spans = list(doc.sents)
    #displacy.serve(sentence_spans, style="ent")
    displacy.serve(sentence_spans, style="dep")

def sanitize_string(var1):
    var1 = re.sub(r', [+-]\d+\.\d+%', "", var1) #ticker value
    var1 = re.sub(r'[Ii]nc.', "Inc", var1) #Inc sentence
    var1 = re.sub(r'\([^()]*\)', " ", var1) #perens
    var1 = re.sub(r'(\\u201c)|(\\u201d)|(\\u201f)|(\\u2033)|(\\u2036)', "\"", var1)
    var1 = re.sub(r'(\\u2018)|(\\u2019)|(\\u201b)|(\\u2032)|(\\u2035)', "\'", var1)
    var1 = re.sub(r'\\u[0-9a-f]{4}', "", var1)
#var1 = var1.replace("%", " percent")
    return var1

if __name__ == '__main__':
    var1 = r'''
    Although Apple does not break down sales of AirPods, the company reported in January that its "other" product category, which includes AirPod sales, grew 33% to $7.3 from a year earlier, the fastest growing category.
    Guy Rosen, Facebook\u2019s FB, +0.84%   \u2016vice president for integrity, said in comments posted late Wednesday that the company\u2019s artificial intelligence tools initially failed to catch the shooter\u2019s live video of the terrorist attack Christchurch mosques last week that killed 50 people.
    On Wednesday, Apple introduced its second generation wireless AirPods.
    .On Wednesday, Apple introduced its second generation wireless AirPods. They will have 50% more talk time, a hands-free \u201chey, Siri!\u201d voice-assistant feature and the option of a wireless charging case. They are, however, just as easy to lose.'''
    #SAN FRANCISCO, March 22, 2019 /PRNewswire/ -- Pinterest, Inc. (\"Pinterest\") today announced that it has filed a registration statement on Form S-1 with the U.S. Securities and Exchange Commission (\"SEC\") relating to a proposed initial public offering of shares of its Class A common stock. The number of shares to be offered and the price range for the proposed offering have not yet been determined.Goldman Sachs & Co. LLC, J.P. Morgan Securities LLC and Allen & Company LLC will serve as lead joint book-running managers for the offering. BofA Merrill Lynch, Barclays Capital Inc.,  Citigroup Global Markets Inc., Credit Suisse Securities (USA) LLC, Deutsche Bank Securities Inc. and RBC Capital Markets, LLC will also act as book-running managers for the offering.  Robert W. Baird & Co. Incorporated, UBS Securities LLC and Wells Fargo Securities, LLC will serve as co-managers for the offering.The offering will be made only by means of a prospectus. Copies of the preliminary prospectus relating to the offering, when available, may be obtained from Goldman Sachs & Co. LLC, Prospectus Department, 200 West Street, New York, NY 10282, telephone: 1-866-471-2526 or by emailing Prospectus-ny@ny.email.gs.com; J.P. Morgan Securities LLC, c/o Broadridge Financial Solutions, 1155 Long Island Avenue, Edgewood, NY 11717, phone: 866-803-9204, email: prospectus-eq_fi@jpmchase.com; or Allen & Company, Prospectus Department, 711 Fifth Avenue, 10th Floor, New York, NY 10022, email: dweidlein@allenco.com. A registration statement relating to these securities has been filed with the SEC, but has not yet become effective. These securities may not be sold nor may offers to buy be accepted prior to the time the registration statement becomes effective. This press release shall not constitute an offer to sell or the solicitation of an offer to buy these securities, nor shall there be any sale of these securities in any state or jurisdiction in which such offer, solicitation or sale would be unlawful prior to registration or qualification under the securities laws of any such state or jurisdiction.Contacts:press@pinterest.comir@pinterest.comView original content:http://www.prnewswire.com/news-releases/pinterest-files-registration-statement-with-sec-for-proposed-initial-public-offering-300817263.htmlSOURCE PinterestCopyright (C) 2019 PR Newswire. All rights reserved
    #American Airlines 'cannot' forecast costs of grounding of 737 MAX aircraft because of uncertainties
    #American Airlines Group Inc. AAL, +0.03% disclosed Monday that its expects the Federal Aviation Administration's grounding of Boeing Co.'s BA, +1.02% 737 MAX aircraft to continue to cause "significant disruption" to its customers and financial costs to the airline. The company said, however, that the financial costs of the disruption "cannot be forecasted at this time," as they will depend on a number of factors, including the period of time of the grounding and the circumstances related to the reintroduction of the aircraft. American said in a filing with the SEC that its fleet included 24 Boeing MAX 8 aircraft, with an additional 76 aircraft on order. Prior to the grounding, it had been operating on average about 90 flights a day involving the grounded aircraft, with flight cancellations announced through April 24, so far. American's stock slipped 0.1% in premarket trade. It has shed 4.8% year to date, while Boeing shares have rallied 12.3%, the NYSE Arca Airline Index XAL, -0.33% has gained 4.5% and the Dow Jones Industrial Average DJIA, +0.23% has advanced 9.3%."""

    #var1 = """
    #Ford Motor Co. F, -0.27% new chief financial officer Tim Stone, who will succeed retiring CFO Bob Shanks on June 1, will \"certainly need to learn the business,\" but there are positives from his background, analysts at RBC said in a note Thursday. Before Stone's brief stint as CFO of Snap Inc. SNAP, -0.47% he worked in finance at Amazon.com Inc. AMZN, -0.23% for 20 years."""

    print(var1)
    var1 = sanitize_string(var1)
    print("sanitized:", var1)
    #var1 = resolve_correfs(var1)
    #print("correfs:", var1)
    extract_triple(var1)
    visualize(var1)


    

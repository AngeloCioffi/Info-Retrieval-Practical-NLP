#!/usr/bin/env python

import neo4j 
#from neo4j import GraphDatabase

driver = neo4j.GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

def add_triple(tx, company, date, URL, verb, sub_pn, sub, obj_pn, obj ):
    tx.run("MERGE (c:Company {name: $company}) "
           "MERGE (a:Article {url: $url, date: $date}) "
           "MERGE (t:Triple {verb: $verb, sub: $sub, obj: $obj}) "
           "MERGE (a)-[:about]->(c) "
           "MERGE (t)-[:in]->(a) ",
        company=company, url=URL, date=date, verb=verb, sub=sub, obj=obj )
    if sub_pn:
        tx.run("MERGE (s:PN {text:sub_pn})-[:subj]->(t)",
            sub_pn=sub_pn )
    if obj_pn:
        tx.run("MERGE (o:PN {text:obj_pn})-[:obj]->(t)",
            obj_pn=obj_pn )

with driver.session() as session:
    session.write_transaction(add_triple, "Apple", "Jan 1, 2019", "http://foo.com", "offers", "Apple Card", "new Apple Card", "", "second best program")

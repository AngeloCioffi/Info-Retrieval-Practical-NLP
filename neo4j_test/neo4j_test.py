#!/usr/bin/env python

from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

def add_triple(tx, company, date, URL, verb, sub_pn, sub, obj_pn, obj ):
    query = ("MERGE (c:Company {name: $company}) "
             "MERGE (a:Article {url: $url, date: $date}) "
             "MERGE (a)-[:about]->(c) "
             "MERGE (t:Triple {verb: $verb, sub: $sub, obj: $obj})-[:in]->(a) ")
    if sub_pn:
        query += ("MERGE (s:PN {text:$sub_pn})"
            "CREATE (s)-[:subj]->(t) ")
    if obj_pn:
        query += ("MERGE (o:PN {text:$obj_pn})"
            "CREATE (o)-[:obj]->(t) ")
    
    tx.run(query, company=company, url=URL, date=date, verb=verb, sub=sub, obj=obj,
            sub_pn=sub_pn,
            obj_pn=obj_pn )

def create_triple(company, date, URL, verb, sub_pn, sub, obj_pn, obj ):
    with driver.session() as session:
        session.write_transaction(add_triple, company, date, URL, verb, sub_pn, sub, obj_pn, obj )

if __name__ == '__main__':
    with driver.session() as session:
        session.write_transaction(add_triple, "Apple", "Jan 1, 2019", "http://foo.com", "offers", "Apple Card", "new Apple Card", "", "second best program")
        session.write_transaction(add_triple, "Apple", "Jan 1, 2019", "http://foo.com", "offers", "Apple Card", "foo Apple Card", "", "foo second best program")
        session.write_transaction(add_triple, "Apple", "Jan 1, 2019", "http://foo.com", "offers", "", "foo2", "Apple Card", "foo2 Apple Card")
        session.write_transaction(add_triple, "Apple", "Jan 2, 2019", "http://foo2.com", "offers", "", "foo2", "Apple Card", "foo2 Apple Card")

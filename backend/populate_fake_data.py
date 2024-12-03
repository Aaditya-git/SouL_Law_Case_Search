from elasticsearch import Elasticsearch, helpers
from faker import Faker

# Elasticsearch connection details
ELASTIC_URL = "https://localhost:9200"
ELASTIC_USER = "elastic"
ELASTIC_PASSWORD = "ADyv8-XWV6=RGfASK9XE"


es = Elasticsearch(
    ELASTIC_URL,
    basic_auth=(ELASTIC_USER, ELASTIC_PASSWORD),
    verify_certs=False  
)


fake = Faker()


mock_cases = {
    "USA": [
        {"case_title": "Brown v. Board of Education", "case_summary": "Landmark case declaring segregation in public schools unconstitutional.", "court": "U.S. Supreme Court", "decision_date": "1954-05-17", "involved_parties": ["Oliver Brown", "Board of Education of Topeka"], "legal_topics": ["Constitutional Law", "Civil Rights"], "country": "USA", "case_link": "https://www.oyez.org/cases/1952/893"},
        {"case_title": "Roe v. Wade", "case_summary": "Landmark decision legalizing abortion across the United States.", "court": "U.S. Supreme Court", "decision_date": "1973-01-22", "involved_parties": ["Jane Roe", "Henry Wade"], "legal_topics": ["Constitutional Law", "Reproductive Rights"], "country": "USA", "case_link": "https://www.oyez.org/cases/1971/70-18"},
        {"case_title": "Miranda v. Arizona", "case_summary": "The Court ruled that detained suspects must be informed of their rights.", "court": "U.S. Supreme Court", "decision_date": "1966-06-13", "involved_parties": ["Ernesto Miranda", "State of Arizona"], "legal_topics": ["Criminal Law", "Constitutional Law"], "country": "USA", "case_link": "https://www.oyez.org/cases/1965/759"},
        {"case_title": "Marbury v. Madison", "case_summary": "Established the principle of judicial review.", "court": "U.S. Supreme Court", "decision_date": "1803-02-24", "involved_parties": ["William Marbury", "James Madison"], "legal_topics": ["Constitutional Law", "Judicial Review"], "country": "USA", "case_link": "https://www.oyez.org/cases/1803/5"},
        {"case_title": "United States v. Nixon", "case_summary": "Ordered Nixon to surrender Watergate tapes, leading to his resignation.", "court": "U.S. Supreme Court", "decision_date": "1974-07-24", "involved_parties": ["United States", "Richard Nixon"], "legal_topics": ["Constitutional Law", "Executive Power"], "country": "USA", "case_link": "https://www.oyez.org/cases/1973/73-1766"},
        {"case_title": "Gideon v. Wainwright", "case_summary": "Defendants in criminal cases must be provided an attorney if they cannot afford one.", "court": "U.S. Supreme Court", "decision_date": "1963-03-18", "involved_parties": ["Clarence Gideon", "Louie Wainwright"], "legal_topics": ["Criminal Law", "Constitutional Law"], "country": "USA", "case_link": "https://www.oyez.org/cases/1962/155"},
        {"case_title": "Loving v. Virginia", "case_summary": "Struck down laws banning interracial marriage.", "court": "U.S. Supreme Court", "decision_date": "1967-06-12", "involved_parties": ["Richard Loving", "Mildred Loving"], "legal_topics": ["Civil Rights", "Family Law"], "country": "USA", "case_link": "https://www.oyez.org/cases/1966/395"},
        {"case_title": "Plessy v. Ferguson", "case_summary": "Upheld 'separate but equal' doctrine for racial segregation.", "court": "U.S. Supreme Court", "decision_date": "1896-05-18", "involved_parties": ["Homer Plessy", "State of Louisiana"], "legal_topics": ["Civil Rights", "Constitutional Law"], "country": "USA", "case_link": "https://www.oyez.org/cases/1895/210"},
        {"case_title": "Tinker v. Des Moines", "case_summary": "Students have free speech rights at school as long as it doesn’t disrupt education.", "court": "U.S. Supreme Court", "decision_date": "1969-02-24", "involved_parties": ["John Tinker", "Mary Beth Tinker", "Des Moines School District"], "legal_topics": ["Constitutional Law", "Civil Rights"], "country": "USA", "case_link": "https://www.oyez.org/cases/1968/21"},
        {"case_title": "Bush v. Gore", "case_summary": "Resolved the 2000 election dispute, stopping a recount in Florida.", "court": "U.S. Supreme Court", "decision_date": "2000-12-12", "involved_parties": ["George W. Bush", "Al Gore"], "legal_topics": ["Election Law", "Constitutional Law"], "country": "USA", "case_link": "https://www.oyez.org/cases/2000/00-949"}
    ],
    "India": [
        {"case_title": "Kesavananda Bharati v. State of Kerala", "case_summary": "The case upheld the power of Parliament to amend the Constitution, but established the basic structure doctrine.", "court": "Supreme Court of India", "decision_date": "1973-04-24", "involved_parties": ["Kesavananda Bharati", "State of Kerala"], "legal_topics": ["Constitutional Law"], "country": "India", "case_link": "https://indiankanoon.org/doc/1292988/"},
        {"case_title": "Maneka Gandhi v. Union of India", "case_summary": "The Court ruled that the right to travel abroad was part of the right to personal liberty under Article 21.", "court": "Supreme Court of India", "decision_date": "1978-01-25", "involved_parties": ["Maneka Gandhi", "Union of India"], "legal_topics": ["Constitutional Law", "Civil Rights"], "country": "India", "case_link": "https://indiankanoon.org/doc/1064649/"},
        {"case_title": "S R Bommai v. Union of India", "case_summary": "Reaffirmed the position of federalism in India and the Court’s role in preventing unconstitutional dismissals of state governments.", "court": "Supreme Court of India", "decision_date": "1994-10-11", "involved_parties": ["S. R. Bommai", "Union of India"], "legal_topics": ["Constitutional Law"], "country": "India", "case_link": "https://indiankanoon.org/doc/1078722/"},
        {"case_title": "Indian Young Lawyers Association v. State of Kerala", "case_summary": "This case allowed women of all ages to enter the Sabarimala temple, challenging the practice of banning women of menstruating age.", "court": "Supreme Court of India", "decision_date": "2018-09-28", "involved_parties": ["Indian Young Lawyers Association", "State of Kerala"], "legal_topics": ["Civil Rights", "Religious Freedom"], "country": "India", "case_link": "https://indiankanoon.org/doc/204100319/"},
        {"case_title": "Navtej Singh Johar v. Union of India", "case_summary": "Decriminalized homosexuality by reading down Section 377 of the Indian Penal Code.", "court": "Supreme Court of India", "decision_date": "2018-09-06", "involved_parties": ["Navtej Singh Johar", "Union of India"], "legal_topics": ["Constitutional Law", "Civil Rights"], "country": "India", "case_link": "https://indiankanoon.org/doc/184266117/"},
        {"case_title": "Shah Bano Case", "case_summary": "A landmark case where the Supreme Court directed the Muslim community to provide maintenance for a divorced woman.", "court": "Supreme Court of India", "decision_date": "1985-04-23", "involved_parties": ["Shah Bano", "Mohammad Ahmad Khan"], "legal_topics": ["Family Law", "Women's Rights"], "country": "India", "case_link": "https://indiankanoon.org/doc/1037262/"},
        {"case_title": "D K Basu v. State of West Bengal", "case_summary": "The Court set guidelines for arrest and detention to prevent police brutality.", "court": "Supreme Court of India", "decision_date": "1997-12-18", "involved_parties": ["D K Basu", "State of West Bengal"], "legal_topics": ["Criminal Law", "Human Rights"], "country": "India", "case_link": "https://indiankanoon.org/doc/1801105/"},
        {"case_title": "Indira Gandhi v. Raj Narain", "case_summary": "The Court ruled that the election of Indira Gandhi was void due to electoral malpractice.", "court": "Supreme Court of India", "decision_date": "1975-06-24", "involved_parties": ["Indira Gandhi", "Raj Narain"], "legal_topics": ["Election Law", "Constitutional Law"], "country": "India", "case_link": "https://indiankanoon.org/doc/2045132/"},
        {"case_title": "Vishaka v. State of Rajasthan", "case_summary": "The Court laid down guidelines for preventing sexual harassment at the workplace.", "court": "Supreme Court of India", "decision_date": "1997-08-13", "involved_parties": ["Vishaka", "State of Rajasthan"], "legal_topics": ["Women's Rights", "Labor Law"], "country": "India", "case_link": "https://indiankanoon.org/doc/1649647/"},
        {"case_title": "M.C. Mehta v. Union of India", "case_summary": "Addressed environmental pollution issues in the country and enforced strict environmental laws.", "court": "Supreme Court of India", "decision_date": "1986-12-03", "involved_parties": ["M.C. Mehta", "Union of India"], "legal_topics": ["Environmental Law", "Public Interest Litigation"], "country": "India", "case_link": "https://indiankanoon.org/doc/831547/"},
    ],
    "Canada": [
        {"case_title": "R v. Morgentaler", "case_summary": "The Court struck down Canada's abortion law, stating it was unconstitutional.", "court": "Supreme Court of Canada", "decision_date": "1988-01-28", "involved_parties": ["Henry Morgentaler", "Canada"], "legal_topics": ["Criminal Law", "Reproductive Rights"], "country": "Canada", "case_link": "https://scc-csc.lexum.com/scc-csc/scc-csc/en/item/444/index.do"},
        {"case_title": "R v. Oakes", "case_summary": "Established the Oakes Test, which is used to determine the limits of rights under the Canadian Charter of Rights and Freedoms.", "court": "Supreme Court of Canada", "decision_date": "1986-05-22", "involved_parties": ["R v. Oakes", "Canada"], "legal_topics": ["Constitutional Law"], "country": "Canada", "case_link": "https://scc-csc.lexum.com/scc-csc/scc-csc/en/item/150/index.do"},
        {"case_title": "Vriend v. Alberta", "case_summary": "Extended human rights protections to sexual orientation under Alberta’s human rights legislation.", "court": "Supreme Court of Canada", "decision_date": "1998-03-20", "involved_parties": ["Vriend", "Alberta"], "legal_topics": ["Civil Rights", "Human Rights"], "country": "Canada", "case_link": "https://scc-csc.lexum.com/scc-csc/scc-csc/en/item/1654/index.do"},
        {"case_title": "R v. Jordan", "case_summary": "The Court set time limits for criminal trials to ensure timely justice in Canada.", "court": "Supreme Court of Canada", "decision_date": "2016-07-08", "involved_parties": ["R v. Jordan", "Canada"], "legal_topics": ["Criminal Law", "Constitutional Law"], "country": "Canada", "case_link": "https://scc-csc.lexum.com/scc-csc/scc-csc/en/item/16122/index.do"},
        {"case_title": "R v. Gladue", "case_summary": "Recognized the need for special consideration for Indigenous people in sentencing.", "court": "Supreme Court of Canada", "decision_date": "1999-04-23", "involved_parties": ["R v. Gladue", "Canada"], "legal_topics": ["Indigenous Law", "Criminal Law"], "country": "Canada", "case_link": "https://scc-csc.lexum.com/scc-csc/scc-csc/en/item/1771/index.do"},
        {"case_title": "Carter v. Canada", "case_summary": "Decriminalized assisted suicide in Canada for competent adults.", "court": "Supreme Court of Canada", "decision_date": "2015-02-06", "involved_parties": ["Carter", "Canada"], "legal_topics": ["Civil Rights", "Health Law"], "country": "Canada", "case_link": "https://scc-csc.lexum.com/scc-csc/scc-csc/en/item/15267/index.do"},
        {"case_title": "Ontario v. Canada", "case_summary": "Clarified the division of powers between the federal and provincial governments.", "court": "Supreme Court of Canada", "decision_date": "1937-01-02", "involved_parties": ["Ontario", "Canada"], "legal_topics": ["Constitutional Law"], "country": "Canada", "case_link": "https://scc-csc.lexum.com/scc-csc/scc-csc/en/item/6162/index.do"},
        {"case_title": "R v. Sparrow", "case_summary": "Affirmed the constitutional protection of Aboriginal fishing rights.", "court": "Supreme Court of Canada", "decision_date": "1990-03-05", "involved_parties": ["R v. Sparrow", "Canada"], "legal_topics": ["Indigenous Law", "Criminal Law"], "country": "Canada", "case_link": "https://scc-csc.lexum.com/scc-csc/scc-csc/en/item/468/index.do"},
        {"case_title": "R v. Keegstra", "case_summary": "Affirmed that hate speech is not protected under the Canadian Charter of Rights.", "court": "Supreme Court of Canada", "decision_date": "1990-12-13", "involved_parties": ["R v. Keegstra", "Canada"], "legal_topics": ["Criminal Law", "Human Rights"], "country": "Canada", "case_link": "https://scc-csc.lexum.com/scc-csc/scc-csc/en/item/582/index.do"},
        {"case_title": "R v. Zundel", "case_summary": "Dealt with the issue of free speech and Holocaust denial in Canada.", "court": "Supreme Court of Canada", "decision_date": "1992-02-27", "involved_parties": ["R v. Zundel", "Canada"], "legal_topics": ["Criminal Law", "Human Rights"], "country": "Canada", "case_link": "https://scc-csc.lexum.com/scc-csc/scc-csc/en/item/563/index.do"}
    ]
}


index_mapping = {
    "mappings": {
        "properties": {
            "case_title": {"type": "text"},
            "case_summary": {"type": "text"},
            "court": {"type": "keyword"},
            "decision_date": {"type": "date"},
            "involved_parties": {"type": "keyword"},
            "legal_topics": {"type": "keyword"},
            "country": {"type": "keyword"},
            "case_link": {"type": "keyword"}
        }
    }
}


if es.indices.exists(index="case_laws"):
    es.indices.delete(index="case_laws")
    print("Deleted existing index: case_laws")


if not es.indices.exists(index="case_laws"):
    es.indices.create(index="case_laws", body=index_mapping)


def prepare_bulk_data(country, case_data):
    actions = []
    for case in case_data:
        case_id = fake.uuid4()  
        action = {
            "_op_type": "index",
            "_index": "case_laws",
            "_id": case_id,
            "_source": case
        }
        actions.append(action)
    return actions

# Index the cases in bulk
def index_cases_in_bulk():
    all_actions = []
    for country, cases in mock_cases.items():
        actions = prepare_bulk_data(country, cases)
        all_actions.extend(actions)
    
    
    helpers.bulk(es, all_actions)


index_cases_in_bulk()

print("Bulk indexing complete!")

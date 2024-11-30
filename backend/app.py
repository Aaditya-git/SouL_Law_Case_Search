from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from elasticsearch import Elasticsearch
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to Elasticsearch
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "ADyv8-XWV6=RGfASK9XE"),
    verify_certs=False
)

# API Routes
@app.get("/cases/")
async def search_cases(query: str, country: str = None):
    """
    Search for cases in Elasticsearch using a multi-match query and filter by country.
    """
    try:
        query_body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "query": query,
                                "fields": ["case_title", "case_summary", "legal_topics"]
                            }
                        }
                    ],
                    "filter": []
                }
            }
        }

        # Add country filter if provided
        if country:
            query_body["query"]["bool"]["filter"].append({"term": {"country": country}})

        response = es.search(index="case_laws", body=query_body)
        
        # Return a list of cases including mock rating
        cases = [
            {
                **hit["_source"],
                "rating": 4,  # You can set mock rating here, ideally you would have this from your dataset
                "case_link": hit["_source"].get("case_link", "#")  # Ensure case link exists
            }
            for hit in response["hits"]["hits"]
        ]

        return {"cases": cases}
    except Exception as e:
        return {"error": str(e)}

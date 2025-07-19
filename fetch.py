import requests
import csv

def fetch_pubmed(query, max_results=20):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    ids = data['esearchresult']['idlist']
    return ids

if __name__ == "__main__":
    query = "biotech OR pharmaceutical"
    ids = fetch_pubmed(query)
    print(f"Fetched PubMed IDs: {ids}")

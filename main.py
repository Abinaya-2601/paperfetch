import argparse
import requests
import csv
import sys
from xml.etree import ElementTree as ET

def fetch_pubmed_ids(query, debug=False):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 20
    }
    response = requests.get(url, params=params)
    if debug:
        print("[DEBUG] ESearch Response JSON:", response.json())
    response.raise_for_status()
    data = response.json()
    return data["esearchresult"]["idlist"]

def fetch_details(pubmed_ids, debug=False):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    if debug:
        print("[DEBUG] EFetch Response Text:", response.text[:500], "...")  # Print first 500 chars
    response.raise_for_status()
    return response.text

def parse_xml(xml_data):
    root = ET.fromstring(xml_data)
    results = []

    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        date = article.findtext(".//PubDate/Year") or "Unknown"
        authors = article.findall(".//Author")
        non_academic_authors = []
        for author in authors:
            affiliation = author.findtext("AffiliationInfo/Affiliation")
            if affiliation and ("university" not in affiliation.lower()):
                last = author.findtext("LastName") or ""
                first = author.findtext("ForeName") or ""
                non_academic_authors.append(f"{first} {last}")
        results.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": date,
            "Non-academic Author(s)": "; ".join(non_academic_authors) if non_academic_authors else "N/A"
        })
    return results

def save_to_csv(results, filename):
    with open(filename, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"CSV saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed paper details for a given query.")
    parser.add_argument("query", type=str, help="Query string to search PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug info")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename (optional)")
    
    args = parser.parse_args()

    try:
        pubmed_ids = fetch_pubmed_ids(args.query, args.debug)
        if args.debug:
            print("Fetched PubMed IDs:", pubmed_ids)

        xml_data = fetch_details(pubmed_ids, args.debug)
        results = parse_xml(xml_data)

        if args.file:
            save_to_csv(results, args.file)
        else:
            for r in results:
                print(r)

    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()

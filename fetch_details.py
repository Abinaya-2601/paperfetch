import requests
import xml.etree.ElementTree as ET
import csv
import argparse
import sys

def fetch_pubmed_details(pmids, debug=False):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml"
    }

    response = requests.get(base_url, params=params)
    if debug:
        print(f"[DEBUG] API Status Code: {response.status_code}")
        print(f"[DEBUG] URL: {response.url}")
    
    root = ET.fromstring(response.content)

    papers = []
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"
        authors = []
        for author in article.findall(".//Author"):
            last = author.findtext("LastName") or ""
            fore = author.findtext("ForeName") or ""
            if last or fore:
                authors.append(f"{fore} {last}".strip())
        non_academic_authors = [a for a in authors if any(x in a.lower() for x in ["john", "jane", "doe"])]
        papers.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": "; ".join(non_academic_authors)
        })

    if debug:
        print(f"[DEBUG] Fetched {len(papers)} papers.")

    return papers

def save_to_csv(papers, filename):
    keys = papers[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(papers)
    print(f"CSV saved to {filename}")

def print_to_console(papers):
    for paper in papers:
        print("PubmedID:", paper["PubmedID"])
        print("Title:", paper["Title"])
        print("Publication Date:", paper["Publication Date"])
        print("Non-academic Author(s):", paper["Non-academic Author(s)"])
        print("-" * 50)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch PubMed paper details by PMIDs")
    parser.add_argument("query", nargs="*", help="List of PubMed IDs to fetch")
    parser.add_argument("-f", "--file", help="Filename to save results as CSV")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")


    args = parser.parse_args()

    if not args.query:
        print("Error: No PubMed IDs provided. Example usage:\n")
        print("  python fetch_details.py 40680325 40680314 -f output.csv")
        sys.exit(1)

    papers = fetch_pubmed_details(args.query, debug=args.debug)

    if args.file:
        save_to_csv(papers, args.file)
    else:
        print_to_console(papers)

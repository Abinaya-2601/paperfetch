# get_papers/get_papers.py

def main():
    import argparse
    import requests
    import csv

    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="PubMed search query")
    parser.add_argument("-f", "--filename", default="results.csv", help="Output CSV file")
    args = parser.parse_args()

    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={args.query}&retmode=json&retmax=5"
    ids = requests.get(url).json()["esearchresult"]["idlist"]

    with open(args.filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["PubMed ID"])
        for pid in ids:
            writer.writerow([pid])
    print(f"Saved {len(ids)} paper IDs to {args.filename}")

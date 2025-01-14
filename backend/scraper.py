# scraper.py
import requests
from bs4 import BeautifulSoup
import json

CDP_SOURCES = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

def scrape_docs():
    """
    A very basic scraper that grabs the main page 
    of each doc site and extracts some paragraphs.
    """
    all_docs = []

    for cdp_name, url in CDP_SOURCES.items():
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                paragraphs = soup.find_all('p')
                for p in paragraphs:
                    text = p.get_text(strip=True)
                    if text:
                        all_docs.append({
                            "platform": cdp_name,
                            "content": text,
                            "url": url
                        })
        except Exception as e:
            print(f"Error scraping {cdp_name} from {url}: {e}")

    # Save to JSON
    with open("data/cdp_docs.json", "w", encoding='utf-8') as f:
        json.dump(all_docs, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    scrape_docs()
    print("Scraping finished. cdp_docs.json created/updated.")

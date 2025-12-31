import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag

visited_url = set()
headers = {"User-Agent": "Mozilla/5.0"}

def spider_url(url, keyword):
    url = url.rstrip("/")
    
    if url in visited_url:
        return

    visited_url.add(url)

    try:
        response = requests.get(url, headers=headers, timeout=5)
        
    except requests.RequestException:
        print(f"Request failed: {url}")
        return

    if response.status_code != 200:
        return

    soup = BeautifulSoup(response.content, "html.parser")

    for anchor_tag in soup.find_all("a"):
        href = anchor_tag.get("href")
        if not href:
            continue

        full_url = urljoin(url, href)
        full_url, _ = urldefrag(full_url)
        full_url = full_url.rstrip("/")

        if full_url in visited_url:
            continue

        if keyword in full_url:
            print(full_url)

        spider_url(full_url, keyword)


url = input(f"Enter the URL: ").strip()
keyword = input("Enter the keyword: ").strip()

spider_url(url, keyword)


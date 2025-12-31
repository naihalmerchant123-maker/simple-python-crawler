# simple-python-crawler
About This Project
This project was initially inspired by a YouTube tutorial on building a basic Python web crawler.
I rewrote and modified the code while learning, and extended it with additional improvements to make it more practical and reliable.


# Modifications & Improvements Made
- Compared to the original tutorial version, I added:
- Custom User-Agent headers to avoid request blocking
- Timeout handling for HTTP requests
- Improved error handling and logging
- URL fragment removal using urldefrag
- URL normalization to reduce duplicate crawling
- Cleaner and safer crawling logic

# Technologies Used
- Python 3
- requests – for making HTTP requests
- BeautifulSoup (bs4) – for parsing HTML
- urllib.parse – for URL joining and fragment removal

- How It Works (Logic Overview)
> Start from a user-provided URL
> Fetch the page content using requests
> Extract all <a> tags using BeautifulSoup
> Convert relative URLs to absolute URLs
> Normalize URLs to avoid duplicates
> Recursively crawl unvisited links
> Print URLs that contain the given keyword

1️⃣ Install dependencies
pip install requests beautifulsoup4

2️⃣ Run the script
python crawler.py

3️⃣ Input
Enter the URL: https://example.com
Enter the keyword: admin

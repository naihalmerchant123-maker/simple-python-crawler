# simple-python-crawler
A simple Python-based recursive web crawler that traverses a website, discovers internal links, and prints URLs that contain a specified keyword.
This project was built as a learning exercise to understand web scraping, recursion, URL normalization, and basic crawling logic using Python.


#Features
- Recursive crawling of web pages
- URL normalization (handles relative links, fragments, trailing slashes)
- Duplicate URL prevention using a 'set'
- Keyword-based URL filtering
- Custom User-Agent support
- Graceful error handling for failed requests

Technologies Used
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
